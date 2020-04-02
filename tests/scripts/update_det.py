#! /usr/bin/env python3

# This script is to update references for deterministic integration tests. 
# Before using it, please be sure the reference.  

# general imports
import os
import re
import sys
import subprocess
from optparse import OptionParser
import numpy as np

# find the path to the qtest executable and its parent directory
script_path = os.path.realpath(__file__)
parent_dir  = os.path.dirname(os.path.dirname(script_path))
main_dir = os.path.dirname(parent_dir)
default_dir = os.path.join(main_dir,"build")

label = "deterministic"
tol = 1.0e-6


if __name__=='__main__':

    parser = OptionParser(
       usage='usage: %prog [options]',
       add_help_option=False,
       )
    parser.add_option('-h','--help',dest='help',
                     action='store_true',default=False,
                     help='Print help information and exit (default=%default).'
                     )
    parser.add_option('-d','--directory',dest='directory',
                     default=default_dir,
                    help='Directory for QMCPACK build to read CMakeCache.txt (default=%default).'
                     )


    options,files_in = parser.parse_args()

    if options.help:
     print('\n'+parser.format_help().strip())
     exit()
    #end if

    cmake_cache = os.path.join(options.directory,"CMakeCache.txt")

    for l in open(cmake_cache,'r').read().splitlines():
     if l.find('EXECUTABLE_OUTPUT_PATH')!=-1: 
      sline = l.split('=')
      bin_dir = sline[1]
     if l.find('qmcpack_SOURCE_DIR')!=-1:
      sline = l.split('=')
      source_dir = sline[1]
   

    qmc_setting = os.path.join(bin_dir,"qmcpack.settings")
    ctest_dir = os.path.join(options.directory,"tests")
    test_dir = os.path.join(source_dir,"tests") 

    for l in open(qmc_setting,'r').readlines():
      if l.find('QMC_COMPLEX')!=-1:
       sline = l.split()
       Complex = bool(int(sline[2]))  
      if l.find('QMC_CUDA')!=-1:
       sline = l.split()
       CUDA = bool(int(sline[2]))      
      if l.find('QMC_MIXED_PRECISION')!=-1:
       sline = l.split()
       Mixed_Precision = bool(int(sline[2]))       

    if (Mixed_Precision == True):
     sys.exit("Reference for mixed-precision build is not supported.")
    

    # Run Ctest to produce outputs
    os.chdir(options.directory)
    print('Running CTest to produce scalar files...')
    subprocess.run('%s %s' % ('ctest -R',label),shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL) 
   
    ctest_file = 'CTestTestfile.cmake'     
    cmake_file = 'CMakeLists.txt'
    out_file = 'CMakeLists.txt.bak'

    det_label = ['diamondC_1x1x1_pp',
                 'diamondC_2x1x1_pp',
                 'LiH_dimer_pp']    
    
    test_list = []
    ntest = 0

    for ind in range(len(det_label)):
  
     for paths,dirs,files in os.walk(ctest_dir):
      for name in dirs:
       if label in name and det_label[ind] in name and not "bug" in name:
         replace_list = []
         scalar_set = []
         print('  Now testing '+name)

         filepath = os.path.join(paths,ctest_file)
         testpath = os.path.join(paths,name)
         f = open(filepath,'r')
         test_scalar = []

         for line in f.readlines():
          if line.find('check_scalars')!=-1 and line.find(name)!=-1:
            output = [None]*3
            sl = line.split() 
            sl = [x.replace('add_test(','').replace(')','') for x in sl]
            length = len(sl)
            check_scalar = ' '.join([sl[x] for x in range(1, length)])
            os.chdir(testpath)

            try:
              run_test = subprocess.check_output(check_scalar,shell=True)
            except subprocess.CalledProcessError as fail:
              run_test = fail.output
              print('     Found failing test '+sl[0])
              replace_list.append(sl[0])

            run_test = np.array(run_test.decode().splitlines())

            observ = sl[0].split('-')
            output[0] = observ[len(observ)-1]    

            for i, s in enumerate(run_test):

             if "reference mean value" in s:
              temp = s.split(':') 
              ref_value = float(temp[1])              
              output[1] = temp[1]

             if "computed  mean value" in s:
              temp = s.split(':')
              out_value = float(temp[1])
              output[2] = temp[1]
             
            temp = output[0] + output[1] + output[2]
            scalar_set.append(temp)
                 
 
         if len(replace_list) > 0:
          for rpaths,rdirs,rfiles in os.walk(test_dir):
             for rname in rdirs:
               if det_label[ind] == rname:
                refpath = os.path.join(rpaths,rname)
                rfilepath = os.path.join(refpath,cmake_file)
                ofilepath = os.path.join(refpath,out_file)
                r = open(rfilepath,'r')
                raw = r.read()

                
                text = ''
                lines = []

                contents = raw.splitlines()


                if not os.path.isfile(ofilepath):
                 o  = open(ofilepath,'w')
                 o.write('\n'.join(contents))
                 o.close()

                for line in contents:
                  ls = line.strip()
                  if not ls.startswith('#'):
                    cloc = line.find('#')
                    if cloc!=-1:
                      line = line[:cloc]
                      ls = line.strip()
                    #end if
                    text += line+'\n'
                    lines.append(ls)
                  #end if
                #end for


                istart = 0
                iend   = 0
                rtext  = ''
                while istart!=-1:
                  istart = text.find(name[:-4],istart)
                  if istart!=-1:
                    iend = text.find(')',istart)
                    if iend!=-1:
                      if text[istart:istart+len(name)].strip() == name[:-4].strip():
                       rtext  = text[istart:iend+1]
                    #end if
                    istart = iend
                  #end if
                #end while

                rtext = rtext.split(' ')
              
                ref_set = []

                for i in range(len(rtext)):
                 if rtext[i].find('DET')!=-1:
                   ref_set.append(rtext[i])
            
                if len(ref_set) > 0:
                 if (len(scalar_set) % len(ref_set)) != 0:
                   sys.exit("Wrong number of references. Please check the number of reference on CMakeLists.txt")

                 nscalar = int(len(scalar_set)/len(ref_set))

                clist = []
                cline = []
                 
                for s in range(0,len(ref_set)):
                  iend = 0
                  nline = 0
                  sind = 0
                  fline = 0
                  for line in contents:
                    nline = nline + 1
                    ls = line.find(ref_set[s])
                    if ls!=-1 and line.find('#')==-1 and line.find('APPEND')!=-1 and iend < nscalar:
                     iend = iend + 1
                     for t in range(0,nscalar):
                       it = s*nscalar+t
                       get_value = scalar_set[it].split()
                       cref = line.split('"')
                       cref = cref[3].split(' ')

                       if line.find(get_value[0].strip())!=-1 and abs(float(cref[0])-float(get_value[1].strip())) < tol:
                        sind = sind + 1

                        if abs(float(cref[0])-float(get_value[2].strip())) > tol:
                         clist.append(get_value)
                         cline.append(nline)
                         fline = fline + 1
                    
                     if iend == nscalar:  
                       if iend > sind:
                        if (fline > 0):
                         del cline[-fline:]
                         del clist[-fline:]
                        sind = 0
                        iend = 0
                        fline = 0
                       else:
                        iend = nscalar                    
           
                     
                r.close()
           
               
                if len(cline) != len(replace_list) or len(cline) != len(clist):
                 sys.exit("number of failing tests and references do not match!") 

                                    
                for s in range(0,len(cline)):
                   nline = 0
                   get_value = " ".join(clist[s])
                   get_value = get_value.split()
                   for line in contents:
                    nline = nline + 1
                    if nline == cline[s] and line.find(get_value[0])!=-1:
                     contents[nline-1] = contents[nline-1].replace(get_value[1],get_value[2])

                c  = open(rfilepath,'w')
                c.write('\n'.join(contents))
                c.close()

                ntest = ntest + len(cline)

   

    print('\n Total ',+ntest,' tests have replaced.')
 
