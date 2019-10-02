
import versions
import testing
from testing import value_eq,object_eq

associated_files = dict()

def get_files():
    return testing.collect_unit_test_file_paths('qmcpack_input',associated_files)
#end def get_files


def format_value(v):
    import numpy as np
    s = ''
    if isinstance(v,np.ndarray):
        pad = 12*' '
        s = 'np.array([\n'
        if len(v.shape)==1:
            s += pad
            for vv in v:
                s += format_value(vv)+','
            #end for
            s = s[:-1]
        else:
            for vv in v:
                s += pad + format_value(list(vv))+',\n'
            #end for
            s = s[:-2]
        #end if
        s += '])'
    elif isinstance(v,(str,np.string_)):
        s = "'"+v+"'"
    else:
        s = str(v)
    #end if
    return s
#end def format_value


def make_serial_reference(qi):
    s = qi.serial()
    ref = '    ref = {\n'
    for k in sorted(s.keys()):
        v = s[k]
        ref +="        '{}' : {},\n".format(k,format_value(v))
    #end for
    ref += '        }\n'
    return ref
#end def make_serial_reference


serial_references = dict()


def generate_serial_references():
    import numpy as np

    ref = {
        '_metadata/lattice/units' : 'bohr',
        '_metadata/position/condition' : '0',
        '_metadata/position/datatype' : 'posArray',
        'simulation/calculations/0/blocks' : 70,
        'simulation/calculations/0/checkpoint' : -1,
        'simulation/calculations/0/method' : 'vmc',
        'simulation/calculations/0/move' : 'pbyp',
        'simulation/calculations/0/samplesperthread' : 2,
        'simulation/calculations/0/steps' : 5,
        'simulation/calculations/0/substeps' : 2,
        'simulation/calculations/0/timestep' : 0.3,
        'simulation/calculations/0/walkers' : 1,
        'simulation/calculations/0/warmupsteps' : 20,
        'simulation/calculations/1/blocks' : 80,
        'simulation/calculations/1/checkpoint' : -1,
        'simulation/calculations/1/method' : 'dmc',
        'simulation/calculations/1/move' : 'pbyp',
        'simulation/calculations/1/nonlocalmoves' : 'yes',
        'simulation/calculations/1/steps' : 5,
        'simulation/calculations/1/timestep' : 0.02,
        'simulation/calculations/1/warmupsteps' : 2,
        'simulation/calculations/2/blocks' : 600,
        'simulation/calculations/2/checkpoint' : -1,
        'simulation/calculations/2/method' : 'dmc',
        'simulation/calculations/2/move' : 'pbyp',
        'simulation/calculations/2/nonlocalmoves' : 'yes',
        'simulation/calculations/2/steps' : 5,
        'simulation/calculations/2/timestep' : 0.005,
        'simulation/calculations/2/warmupsteps' : 10,
        'simulation/project/application/class_' : 'serial',
        'simulation/project/application/name' : 'qmcapp',
        'simulation/project/application/role' : 'molecu',
        'simulation/project/application/version' : 1.0,
        'simulation/project/id' : 'qmc',
        'simulation/project/series' : 0,
        'simulation/qmcsystem/hamiltonians/h0/estimators/KEcorr/name' : 'KEcorr',
        'simulation/qmcsystem/hamiltonians/h0/estimators/KEcorr/psi' : 'psi0',
        'simulation/qmcsystem/hamiltonians/h0/estimators/KEcorr/source' : 'e',
        'simulation/qmcsystem/hamiltonians/h0/estimators/KEcorr/type' : 'chiesa',
        'simulation/qmcsystem/hamiltonians/h0/estimators/SpinDensity/grid' : np.array([
            72,44,44]),
        'simulation/qmcsystem/hamiltonians/h0/estimators/SpinDensity/name' : 'SpinDensity',
        'simulation/qmcsystem/hamiltonians/h0/estimators/SpinDensity/type' : 'spindensity',
        'simulation/qmcsystem/hamiltonians/h0/name' : 'h0',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/ElecElec/name' : 'ElecElec',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/ElecElec/source' : 'e',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/ElecElec/target' : 'e',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/ElecElec/type' : 'coulomb',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/IonIon/name' : 'IonIon',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/IonIon/source' : 'ion0',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/IonIon/target' : 'ion0',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/IonIon/type' : 'coulomb',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/MPC/ecut' : 60.0,
        'simulation/qmcsystem/hamiltonians/h0/pairpots/MPC/name' : 'MPC',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/MPC/physical' : False,
        'simulation/qmcsystem/hamiltonians/h0/pairpots/MPC/source' : 'e',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/MPC/target' : 'e',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/MPC/type' : 'MPC',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/format' : 'xml',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/name' : 'PseudoPot',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/pseudos/O/elementtype' : 'O',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/pseudos/O/href' : 'O.opt.xml',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/pseudos/V/elementtype' : 'V',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/pseudos/V/href' : 'V.opt.xml',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/source' : 'ion0',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/type' : 'pseudo',
        'simulation/qmcsystem/hamiltonians/h0/pairpots/PseudoPot/wavefunction' : 'psi0',
        'simulation/qmcsystem/hamiltonians/h0/target' : 'e',
        'simulation/qmcsystem/hamiltonians/h0/type' : 'generic',
        'simulation/qmcsystem/particlesets/e/groups/d/charge' : -1,
        'simulation/qmcsystem/particlesets/e/groups/d/mass' : 1.0,
        'simulation/qmcsystem/particlesets/e/groups/d/name' : 'd',
        'simulation/qmcsystem/particlesets/e/groups/d/size' : 200,
        'simulation/qmcsystem/particlesets/e/groups/u/charge' : -1,
        'simulation/qmcsystem/particlesets/e/groups/u/mass' : 1.0,
        'simulation/qmcsystem/particlesets/e/groups/u/name' : 'u',
        'simulation/qmcsystem/particlesets/e/groups/u/size' : 200,
        'simulation/qmcsystem/particlesets/e/name' : 'e',
        'simulation/qmcsystem/particlesets/e/random' : True,
        'simulation/qmcsystem/particlesets/ion0/groups/O/atomicnumber' : 8,
        'simulation/qmcsystem/particlesets/ion0/groups/O/charge' : 6,
        'simulation/qmcsystem/particlesets/ion0/groups/O/mass' : 29164.3928678,
        'simulation/qmcsystem/particlesets/ion0/groups/O/name' : 'O',
        'simulation/qmcsystem/particlesets/ion0/groups/O/position' : np.array([
            [0.00978311, 1.81708472, 1.78656736],
            [10.85992161, 15.33331378, -1.78656738],
            [2.75326234, 11.04571415, -2.495713],
            [8.1164424, 6.10468435, 2.495713],
            [2.71381355, 6.02493499, 2.55909075],
            [8.15589117, 11.12546351, -2.55909075],
            [5.45729278, 15.41306313, -1.72318961],
            [5.41241194, 1.73733537, 1.72318961],
            [10.87948783, 1.81708472, 1.78656736],
            [21.72962633, 15.33331378, -1.78656738],
            [13.62296706, 11.04571415, -2.495713],
            [18.98614712, 6.10468435, 2.495713],
            [13.58351827, 6.02493499, 2.55909075],
            [19.02559589, 11.12546351, -2.55909075],
            [16.3269975, 15.41306313, -1.72318961],
            [16.28211666, 1.73733537, 1.72318961],
            [0.00978311, 10.39228397, 1.78656736],
            [10.85992161, 6.75811453, -1.78656738],
            [-2.7336961, 11.04571415, 6.06884775],
            [13.60340084, 6.10468435, -6.06884775],
            [8.20077199, 6.02493499, -6.00547],
            [2.66893273, 11.12546351, 6.00547],
            [5.45729278, 6.83786388, -1.72318961],
            [5.41241194, 10.31253462, 1.72318961],
            [10.87948783, 10.39228397, 1.78656736],
            [21.72962633, 6.75811453, -1.78656738],
            [8.13600862, 11.04571415, 6.06884775],
            [24.47310556, 6.10468435, -6.06884775],
            [19.07047671, 6.02493499, -6.00547],
            [13.53863745, 11.12546351, 6.00547],
            [16.3269975, 6.83786388, -1.72318961],
            [16.28211666, 10.31253462, 1.72318961]]),
        'simulation/qmcsystem/particlesets/ion0/groups/O/size' : 32,
        'simulation/qmcsystem/particlesets/ion0/groups/O/valence' : 6,
        'simulation/qmcsystem/particlesets/ion0/groups/V/atomicnumber' : 23,
        'simulation/qmcsystem/particlesets/ion0/groups/V/charge' : 13,
        'simulation/qmcsystem/particlesets/ion0/groups/V/mass' : 92861.5851912,
        'simulation/qmcsystem/particlesets/ion0/groups/V/name' : 'V',
        'simulation/qmcsystem/particlesets/ion0/groups/V/position' : np.array([
            [2.45778327, 8.39460555, 0.22661828],
            [8.41192147, 8.75579295, -0.22661828],
            [5.2012625, 13.04339257, -4.0556621],
            [5.66844224, 4.10700593, 4.0556621],
            [13.32748799, 8.39460555, 0.22661828],
            [19.28162619, 8.75579295, -0.22661828],
            [16.07096722, 13.04339257, -4.0556621],
            [16.53814696, 4.10700593, 4.0556621],
            [7.94474171, 8.39460555, -8.33794247],
            [2.92496303, 8.75579295, 8.33794247],
            [5.2012625, 4.46819332, -4.0556621],
            [5.66844224, 12.68220518, 4.0556621],
            [18.81444643, 8.39460555, -8.33794247],
            [13.79466775, 8.75579295, 8.33794247],
            [16.07096722, 4.46819332, -4.0556621],
            [16.53814696, 12.68220518, 4.0556621]]),
        'simulation/qmcsystem/particlesets/ion0/groups/V/size' : 16,
        'simulation/qmcsystem/particlesets/ion0/groups/V/valence' : 13,
        'simulation/qmcsystem/particlesets/ion0/name' : 'ion0',
        'simulation/qmcsystem/simulationcell/bconds' : np.array([
            'p','p','p']),
        'simulation/qmcsystem/simulationcell/lattice' : np.array([
            [21.73940944, 0.0, 0.0],
            [5.48695844, 8.57519925, -8.56456075],
            [-5.48695844, 8.57519925, 8.56456075]]),
        'simulation/qmcsystem/simulationcell/lr_dim_cutoff' : 15,
        'simulation/qmcsystem/wavefunctions/psi0/determinantset/slaterdeterminant/determinants/downdet/group' : 'd',
        'simulation/qmcsystem/wavefunctions/psi0/determinantset/slaterdeterminant/determinants/downdet/id' : 'downdet',
        'simulation/qmcsystem/wavefunctions/psi0/determinantset/slaterdeterminant/determinants/downdet/size' : 200,
        'simulation/qmcsystem/wavefunctions/psi0/determinantset/slaterdeterminant/determinants/downdet/sposet' : 'spo_d',
        'simulation/qmcsystem/wavefunctions/psi0/determinantset/slaterdeterminant/determinants/updet/group' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/determinantset/slaterdeterminant/determinants/updet/id' : 'updet',
        'simulation/qmcsystem/wavefunctions/psi0/determinantset/slaterdeterminant/determinants/updet/size' : 200,
        'simulation/qmcsystem/wavefunctions/psi0/determinantset/slaterdeterminant/determinants/updet/sposet' : 'spo_u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/O/coefficients/coeff' : np.array([
            -1.488295706,-1.406709163,-1.232298155,-0.9391459067,-0.5575491618,-0.2186131788,-0.1463697747,-0.09781208605,-0.06418209044,-0.03977101442,-0.02226362717,-0.009458557456,-0.002401473122]),
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/O/coefficients/id' : 'eO',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/O/coefficients/type' : 'Array',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/O/cusp' : 0.0,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/O/elementtype' : 'O',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/O/rcut' : 6.05,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/O/size' : 13,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/V/coefficients/coeff' : np.array([
            -2.88368129,-2.686350256,-2.500947608,-2.096756839,-1.444128943,-0.7686333881,-0.5720610092,-0.4061081504,-0.2772741837,-0.1767662649,-0.1010035901,-0.047325819,-0.01700847314]),
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/V/coefficients/id' : 'eV',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/V/coefficients/type' : 'Array',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/V/cusp' : 0.0,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/V/elementtype' : 'V',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/V/rcut' : 6.05,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/correlations/V/size' : 13,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/function' : 'bspline',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/name' : 'J1',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/print_' : True,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/source' : 'ion0',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J1/type' : 'One-Body',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/ud/coefficients/coeff' : np.array([
            0.529300758,0.3529320289,0.2365993762,0.1604582152,0.1128159005,0.08243318778,0.06023602184,0.04310552718,0.02984314449,0.01958170086,0.01186100803,0.006112206499,0.002625360754]),
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/ud/coefficients/id' : 'ud',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/ud/coefficients/type' : 'Array',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/ud/rcut' : 6.05,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/ud/size' : 13,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/ud/speciesa' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/ud/speciesb' : 'd',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/uu/coefficients/coeff' : np.array([
            0.3569086717,0.2751683418,0.2058897032,0.1520886231,0.111693376,0.08181917929,0.05977972383,0.04283213009,0.02968150709,0.01944788064,0.01196129476,0.006271327336,0.002804432275]),
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/uu/coefficients/id' : 'uu',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/uu/coefficients/type' : 'Array',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/uu/rcut' : 6.05,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/uu/size' : 13,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/uu/speciesa' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/correlations/uu/speciesb' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/function' : 'bspline',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/name' : 'J2',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/print_' : True,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J2/type' : 'Two-Body',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/coefficients/coeff' : np.array([
            -0.004166620907,0.0003869059334,0.01344638104,-7.5215692e-05,-0.006436299048,0.0008791813519,0.007681280497,-0.006673633544,0.0300621195,0.00157665002,-0.001657156134,-0.01142258435,-0.02006687607,0.005271171591,0.01511417522,0.0008942941789,-0.002018984988,0.01595864928,0.005244762096,0.01545262066,-0.006397246289,-0.0072233246,-0.0008063061353,0.00830708478,0.001242024926,-0.0003962016339]),
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/coefficients/id' : 'udO',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/coefficients/optimize' : True,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/coefficients/type' : 'Array',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/esize' : 3,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/especies1' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/especies2' : 'd',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/isize' : 3,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/ispecies' : 'O',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udO/rcut' : 5.0,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/coefficients/coeff' : np.array([
            0.000658573315,0.005924655484,0.008096696785,0.002998451182,0.001289481835,8.390092052e-05,0.0174934698,0.004082827829,0.001656608224,-0.01638865932,0.002852247319,-0.01043954065,0.006179637761,-0.000652977982,-0.004542989787,-0.0004825008427,0.03569269894,-0.01539236687,0.007843924995,-0.009660462887,-0.01173827315,0.005074028683,0.001248279616,0.008752252359,-0.003457347502,0.0001174638519]),
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/coefficients/id' : 'udV',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/coefficients/optimize' : True,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/coefficients/type' : 'Array',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/esize' : 3,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/especies1' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/especies2' : 'd',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/isize' : 3,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/ispecies' : 'V',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/udV/rcut' : 5.0,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/coefficients/coeff' : np.array([
            -0.0006976974299,-0.001602461137,0.002262076236,-0.001250356792,-0.002453974076,0.00100226978,-0.008343708726,0.01062739293,0.01589135522,0.007887562739,-0.0005580320441,-0.01523126657,-0.009565046782,-0.0009005995139,0.01105399926,-0.0002575705031,-0.01652920678,0.00747060564,0.01464528142,0.005133083617,0.006916610617,-0.009683594066,0.001290999707,-0.001322800206,0.003931225142,-0.001163411737]),
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/coefficients/id' : 'uuO',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/coefficients/optimize' : True,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/coefficients/type' : 'Array',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/esize' : 3,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/especies1' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/especies2' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/isize' : 3,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/ispecies' : 'O',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuO/rcut' : 5.0,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/coefficients/coeff' : np.array([
            0.004388200165,0.001900643263,-0.01549468789,-0.002564479476,0.002118937653,0.0007437421471,-0.0085007067,0.009637603236,-0.01717900977,0.00186285366,-0.006121695671,0.01831402072,0.006890778761,0.003340289515,-0.001491823024,-0.001123033117,-0.008713157223,0.02100098414,-0.03224060809,-0.002479213835,0.001387768485,0.006636471962,0.0004745014561,0.001629700016,-0.001615344115,-0.0001680854702]),
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/coefficients/id' : 'uuV',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/coefficients/optimize' : True,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/coefficients/type' : 'Array',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/esize' : 3,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/especies1' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/especies2' : 'u',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/isize' : 3,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/ispecies' : 'V',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/correlations/uuV/rcut' : 5.0,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/function' : 'polynomial',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/name' : 'J3',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/print_' : True,
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/source' : 'ion0',
        'simulation/qmcsystem/wavefunctions/psi0/jastrows/J3/type' : 'eeI',
        'simulation/qmcsystem/wavefunctions/psi0/name' : 'psi0',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/href' : '../scf/pwscf_output/pwscf.pwscf.h5',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/meshfactor' : 1.0,
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/precision' : 'float',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/source' : 'ion0',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/sposets/spo_d/name' : 'spo_d',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/sposets/spo_d/size' : 200,
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/sposets/spo_d/spindataset' : 1,
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/sposets/spo_d/type' : 'bspline',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/sposets/spo_u/name' : 'spo_u',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/sposets/spo_u/size' : 200,
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/sposets/spo_u/spindataset' : 0,
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/sposets/spo_u/type' : 'bspline',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/tilematrix' : np.array([
            [2, 0, 0],
            [0, 1, -1],
            [0, 1, 1]]),
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/truncate' : False,
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/twistnum' : 0,
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/type' : 'bspline',
        'simulation/qmcsystem/wavefunctions/psi0/sposet_builders/bspline/version' : 0.1,
        'simulation/qmcsystem/wavefunctions/psi0/target' : 'e',
        }

    serial_references['VO2_M1_afm.in.xml'] = ref
#end def generate_serial_references


def get_serial_references():
    if len(serial_references)==0:
        generate_serial_references()
    #end if
    return serial_references
#end def get_serial_references


def check_vs_serial_reference(qi,name):
    sr = get_serial_references()[name]
    assert(len(sr)>0)
    sq = qi.serial()
    for k in sorted(sr.keys()):
        assert(k in sq)
        assert(value_eq(sq[k],sr[k]))
    #end for
#end def check_vs_serial_reference



def test_files():
    filenames = [
        'VO2_M1_afm.in.xml',
        ]
    files = get_files()
    assert(set(filenames)==set(files.keys()))
#end def test_files



def test_compose():
    import numpy as np
    from generic import obj
    from qmcpack_input import QmcpackInput
    from qmcpack_input import simulation,meta,section

    qi_comp = QmcpackInput(
        meta(
            lattice  = obj(units='bohr'),
            position = obj(condition='0',datatype='posArray'),
            ),
        simulation(
            project = section(
                id     ='qmc',
                series = 0,
                application = section(
                    name    = 'qmcapp',
                    role    = 'molecu',
                    class_  = 'serial',
                    version = 1.0,
                    ),
                ),
            qmcsystem = section(
                simulationcell = section(
                    lattice = np.array(
                        [[ 21.73940944, 0.00000000,  0.00000000],
                         [  5.48695844, 8.57519925, -8.56456075],
                         [ -5.48695844, 8.57519925,  8.56456075]]),
                    bconds = np.array(tuple('ppp')),
                    lr_dim_cutoff = 15,
                    ),
                particlesets = [
                    section(
                        name = 'e',
                        random = True,
                        groups = [
                            section(
                                name   = 'u',
                                size   = 200,
                                charge = -1,
                                mass   = 1.0,
                                ),
                            section(
                                name   = 'd',
                                size   = 200,
                                charge = -1,
                                mass   = 1.0,
                                ),
                            ],
                        ),
                    section(
                        name = 'ion0',
                        groups = [
                            section(
                                name         = 'V',
                                size         = 16,
                                charge       = 13,
                                valence      = 13,
                                atomicnumber = 23,
                                mass         = 92861.5851912,
                                position     = np.array([
                                    [ 2.45778327,  8.39460555,  0.22661828],
                                    [ 8.41192147,  8.75579295, -0.22661828],
                                    [ 5.20126250, 13.04339257, -4.05566210],
                                    [ 5.66844224,  4.10700593,  4.05566210],
                                    [13.32748799,  8.39460555,  0.22661828],
                                    [19.28162619,  8.75579295, -0.22661828],
                                    [16.07096722, 13.04339257, -4.05566210],
                                    [16.53814696,  4.10700593,  4.05566210],
                                    [ 7.94474171,  8.39460555, -8.33794247],
                                    [ 2.92496303,  8.75579295,  8.33794247],
                                    [ 5.20126250,  4.46819332, -4.05566210],
                                    [ 5.66844224, 12.68220518,  4.05566210],
                                    [18.81444643,  8.39460555, -8.33794247],
                                    [13.79466775,  8.75579295,  8.33794247],
                                    [16.07096722,  4.46819332, -4.05566210],
                                    [16.53814696, 12.68220518,  4.05566210]
                                    ]),
                                ),
                            section(
                                name         = 'O',
                                size         = 32,
                                charge       = 6,
                                valence      = 6,
                                atomicnumber = 8,
                                mass         = 29164.3928678,
                                position     = np.array([
                                    [ 0.00978311,  1.81708472,  1.78656736],
                                    [10.85992161, 15.33331378, -1.78656738],
                                    [ 2.75326234, 11.04571415, -2.49571300],
                                    [ 8.11644240,  6.10468435,  2.49571300],
                                    [ 2.71381355,  6.02493499,  2.55909075],
                                    [ 8.15589117, 11.12546351, -2.55909075],
                                    [ 5.45729278, 15.41306313, -1.72318961],
                                    [ 5.41241194,  1.73733537,  1.72318961],
                                    [10.87948783,  1.81708472,  1.78656736],
                                    [21.72962633, 15.33331378, -1.78656738],
                                    [13.62296706, 11.04571415, -2.49571300],
                                    [18.98614712,  6.10468435,  2.49571300],
                                    [13.58351827,  6.02493499,  2.55909075],
                                    [19.02559589, 11.12546351, -2.55909075],
                                    [16.32699750, 15.41306313, -1.72318961],
                                    [16.28211666,  1.73733537,  1.72318961],
                                    [ 0.00978311, 10.39228397,  1.78656736],
                                    [10.85992161,  6.75811453, -1.78656738],
                                    [-2.73369610, 11.04571415,  6.06884775],
                                    [13.60340084,  6.10468435, -6.06884775],
                                    [ 8.20077199,  6.02493499, -6.00547000],
                                    [ 2.66893273, 11.12546351,  6.00547000],
                                    [ 5.45729278,  6.83786388, -1.72318961],
                                    [ 5.41241194, 10.31253462,  1.72318961],
                                    [10.87948783, 10.39228397,  1.78656736],
                                    [21.72962633,  6.75811453, -1.78656738],
                                    [ 8.13600862, 11.04571415,  6.06884775],
                                    [24.47310556,  6.10468435, -6.06884775],
                                    [19.07047671,  6.02493499, -6.00547000],
                                    [13.53863745, 11.12546351,  6.00547000],
                                    [16.32699750,  6.83786388, -1.72318961],
                                    [16.28211666, 10.31253462,  1.72318961]
                                    ]),
                                ),
                            ],
                        ),
                    ],
                wavefunction = section(
                    name   = 'psi0',
                    target = 'e',
                    sposet_builder = section(
                        type       = 'bspline',
                        href       = '../scf/pwscf_output/pwscf.pwscf.h5',
                        tilematrix = np.array([[2,0,0],
                                               [0,1,-1],
                                               [0,1,1]]),
                        twistnum   = 0,
                        source     = 'ion0',
                        version    = 0.10,
                        meshfactor = 1.0,
                        precision  = 'float',
                        truncate   = False,
                        sposets = [
                            section(
                                type        = 'bspline',
                                name        = 'spo_u',
                                size        = 200,
                                spindataset = 0,
                                ),
                            section(
                                type        = 'bspline',
                                name        = 'spo_d',
                                size        = 200,
                                spindataset = 1,
                                )
                            ],
                        ),
                    determinantset = section(
                        slaterdeterminant = section(
                            determinants = [
                                section(
                                    id     = 'updet',
                                    group  = 'u',
                                    sposet = 'spo_u',
                                    size   = 200,
                                    ),
                                section(
                                    id     = 'downdet',
                                    group  = 'd',
                                    sposet = 'spo_d',
                                    size   = 200,
                                    ),
                                ],
                            ),
                        ),
                    jastrows = [
                        section(
                            type     = 'One-Body',
                            name     = 'J1',
                            function = 'bspline',
                            source   = 'ion0',
                            print_   = True,
                            correlations = [
                                section(
                                    elementType = 'O',
                                    size        = 13,
                                    rcut        = 6.05,
                                    cusp        = 0.0,
                                    coefficients = section(
                                        id   = 'eO',
                                        type = 'Array',
                                        coeff = np.array([
                                            -1.488295706, -1.406709163,
                                            -1.232298155, -0.9391459067, 
                                            -0.5575491618, -0.2186131788, 
                                            -0.1463697747, -0.09781208605, 
                                            -0.06418209044, -0.03977101442, 
                                            -0.02226362717, -0.009458557456, 
                                            -0.002401473122])
                                        ),
                                    ),
                                section(
                                    elementType = 'V',
                                    size        = 13,
                                    rcut        = 6.05,
                                    cusp        = 0.0,
                                    coefficients = section(
                                        id   = 'eV',
                                        type = 'Array',
                                        coeff = np.array([
                                            -2.88368129, -2.686350256, 
                                            -2.500947608, -2.096756839, 
                                            -1.444128943, -0.7686333881, 
                                            -0.5720610092, -0.4061081504,
                                            -0.2772741837, -0.1767662649, 
                                            -0.1010035901, -0.047325819, 
                                            -0.01700847314])
                                        ),
                                    ),
                                ],
                            ),
                        section(
                            type     = 'Two-Body',
                            name     = 'J2',
                            function = 'bspline',
                            print_   = True,
                            correlations = [
                                section(
                                    speciesA    = 'u',
                                    speciesB    = 'u',
                                    size        = 13,
                                    rcut        = 6.05,
                                    coefficients = section(
                                        id    = 'uu',
                                        type  = 'Array',
                                        coeff = np.array([
                                            0.3569086717, 0.2751683418, 
                                            0.2058897032, 0.1520886231, 
                                            0.111693376, 0.08181917929, 
                                            0.05977972383, 0.04283213009, 
                                            0.02968150709, 0.01944788064, 
                                            0.01196129476, 0.006271327336, 
                                            0.002804432275])
                                        ),
                                    ),
                                section(
                                    speciesA    = 'u',
                                    speciesB    = 'd',
                                    size        = 13,
                                    rcut        = 6.05,
                                    coefficients = section(
                                        id    = 'ud',
                                        type  = 'Array',
                                        coeff = np.array([
                                            0.529300758, 0.3529320289, 
                                            0.2365993762, 0.1604582152, 
                                            0.1128159005, 0.08243318778, 
                                            0.06023602184, 0.04310552718, 
                                            0.02984314449, 0.01958170086, 
                                            0.01186100803, 0.006112206499, 
                                            0.002625360754])
                                        ),
                                    ),
                                ],
                            ),
                        section(
                            type     = 'eeI',
                            name     = 'J3',
                            function = 'polynomial',
                            print_   = True,
                            source   = 'ion0',
                            correlations = [
                                section(
                                    ispecies = 'O',
                                    especies1= 'u',
                                    especies2= 'u',
                                    isize    = 3,
                                    esize    = 3,
                                    rcut     = 5.0,
                                    coefficients = section(
                                        id       = 'uuO',
                                        type     = 'Array',
                                        optimize = True,
                                        coeff    = np.array([
                                            -0.0006976974299, -0.001602461137, 
                                            0.002262076236, -0.001250356792, 
                                            -0.002453974076, 0.00100226978, 
                                            -0.008343708726, 0.01062739293, 
                                            0.01589135522, 0.007887562739, 
                                            -0.0005580320441, -0.01523126657, 
                                            -0.009565046782, -0.0009005995139, 
                                            0.01105399926, -0.0002575705031, 
                                            -0.01652920678, 0.00747060564, 
                                            0.01464528142, 0.005133083617, 
                                            0.006916610617, -0.009683594066, 
                                            0.001290999707, -0.001322800206, 
                                            0.003931225142, -0.001163411737])
                                        ),
                                    ),
                                section(
                                    ispecies = 'O',
                                    especies1= 'u',
                                    especies2= 'd',
                                    isize    = 3,
                                    esize    = 3,
                                    rcut     = 5.0,
                                    coefficients = section(
                                        id       = 'udO',
                                        type     = 'Array',
                                        optimize = True,
                                        coeff    = np.array([
                                            -0.004166620907, 0.0003869059334, 
                                            0.01344638104, -7.5215692e-05, 
                                            -0.006436299048, 0.0008791813519, 
                                            0.007681280497, -0.006673633544, 
                                            0.0300621195, 0.00157665002, 
                                            -0.001657156134, -0.01142258435, 
                                            -0.02006687607, 0.005271171591, 
                                            0.01511417522, 0.0008942941789, 
                                            -0.002018984988, 0.01595864928, 
                                            0.005244762096, 0.01545262066, 
                                            -0.006397246289, -0.0072233246, 
                                            -0.0008063061353, 0.00830708478, 
                                            0.001242024926, -0.0003962016339])
                                        ),
                                    ),
                                section(
                                    ispecies = 'V',
                                    especies1= 'u',
                                    especies2= 'u',
                                    isize    = 3,
                                    esize    = 3,
                                    rcut     = 5.0,
                                    coefficients = section(
                                        id       = 'uuV',
                                        type     = 'Array',
                                        optimize = True,
                                        coeff    = np.array([
                                            0.004388200165, 0.001900643263, 
                                            -0.01549468789, -0.002564479476, 
                                            0.002118937653, 0.0007437421471, 
                                            -0.0085007067, 0.009637603236, 
                                            -0.01717900977, 0.00186285366, 
                                            -0.006121695671, 0.01831402072,
                                            0.006890778761, 0.003340289515, 
                                            -0.001491823024, -0.001123033117, 
                                            -0.008713157223, 0.02100098414, 
                                            -0.03224060809, -0.002479213835, 
                                            0.001387768485, 0.006636471962, 
                                            0.0004745014561, 0.001629700016, 
                                            -0.001615344115, -0.0001680854702])
                                        ),
                                    ),
                                section(
                                    ispecies = 'V',
                                    especies1= 'u',
                                    especies2= 'd',
                                    isize    = 3,
                                    esize    = 3,
                                    rcut     = 5.0,
                                    coefficients = section(
                                        id       = 'udV',
                                        type     = 'Array',
                                        optimize = True,
                                        coeff    = np.array([
                                            0.000658573315, 0.005924655484, 
                                            0.008096696785, 0.002998451182, 
                                            0.001289481835, 8.390092052e-05, 
                                            0.0174934698, 0.004082827829, 
                                            0.001656608224, -0.01638865932, 
                                            0.002852247319, -0.01043954065, 
                                            0.006179637761, -0.000652977982, 
                                            -0.004542989787, -0.0004825008427, 
                                            0.03569269894, -0.01539236687, 
                                            0.007843924995, -0.009660462887, 
                                            -0.01173827315, 0.005074028683, 
                                            0.001248279616, 0.008752252359, 
                                            -0.003457347502, 0.0001174638519])
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                hamiltonian = section(
                    name   = 'h0',
                    type   = 'generic',
                    target = 'e',
                    pairpots = [
                        section( 
                            type   = 'coulomb',
                            name   = 'ElecElec',
                            source = 'e',
                            target = 'e'
                            ),
                        section(
                            type   = 'coulomb',
                            name   = 'IonIon',
                            source = 'ion0',
                            target = 'ion0'
                            ),
                        section(
                            type         = 'pseudo',
                            name         = 'PseudoPot',
                            source       = 'ion0',
                            wavefunction = 'psi0',
                            format       = 'xml',
                            pseudos = [
                                section(
                                    elementType = 'O',
                                    href        = 'O.opt.xml'
                                    ),
                                section(
                                    elementType = 'V',
                                    href        = 'V.opt.xml'
                                    ),
                                ]
                            ),
                        section(
                            type     = 'MPC',
                            name     = 'MPC',
                            source   = 'e',
                            target   = 'e',
                            ecut     = 60.0,
                            physical = False
                            )
                        ],
                    estimators = [
                        section(
                            type = 'spindensity',
                            name = 'SpinDensity',
                            grid = np.array([72,44,44]),
                            ),
                        section(
                            name   = 'KEcorr',
                            type   = 'chiesa',
                            source = 'e',
                            psi    = 'psi0'
                            )
                        ],
                    )
                ),
            calculations = [
                section(
                    method           = 'vmc',
                    move             = 'pbyp',
                    checkpoint       = -1,
                    walkers          = 1,
                    blocks           = 70,
                    steps            = 5,
                    substeps         = 2,
                    timestep         = 0.3,
                    warmupsteps      = 20,
                    samplesperthread = 2,
                    ),
                section(
                    method           = 'dmc',
                    move             = 'pbyp',
                    checkpoint       = -1,
                    blocks           = 80,
                    steps            = 5,
                    timestep         = 0.02,
                    nonlocalmoves    = 'yes',
                    warmupsteps      = 2,
                    ),
                section(
                    method           = 'dmc',
                    move             = 'pbyp',
                    checkpoint       = -1,
                    blocks           = 600,
                    steps            = 5,
                    timestep         = 0.005,
                    nonlocalmoves    = 'yes',
                    warmupsteps      = 10,
                    ),
                ],
            ),
        )
    qi_comp.pluralize()

    check_vs_serial_reference(qi_comp,'VO2_M1_afm.in.xml')

#end def test_compose



def test_read():
    from qmcpack_input import QmcpackInput

    files = get_files()

    qi_read = QmcpackInput(files['VO2_M1_afm.in.xml'])
    qi_read.pluralize()

    # remove extraneous data members for purpose of comparison
    del qi_read._metadata.spo_u
    del qi_read._metadata.spo_d
    spob = qi_read.simulation.qmcsystem.wavefunctions.psi0.sposet_builders
    sposets = spob.bspline.sposets
    del sposets.spo_u.spos
    del sposets.spo_d.spos

    check_vs_serial_reference(qi_read,'VO2_M1_afm.in.xml')

#end def test_read



def test_write():
    tpath = testing.setup_unit_test_output_directory('qmcpack_input','test_write')
#end def test_write



def test_generate_kspace_jastrow():
    from qmcpack_input import generate_kspace_jastrow
    kjas = generate_kspace_jastrow(1.0, 2.0, 2, 4)
    expect = '''<jastrow type="kSpace" name="Jk" source="ion0">
   <correlation kc="1.0" type="One-Body" symmetry="isotropic">
      <coefficients id="cG1" type="Array">         
0 0
      </coefficients>
   </correlation>
   <correlation kc="2.0" type="Two-Body" symmetry="isotropic">
      <coefficients id="cG2" type="Array">         
0 0 0 0
      </coefficients>
   </correlation>
</jastrow>
'''
    text = kjas.write()
    assert text == expect
#end def test_generate_kspace_jastrow




def test_excited_state():
    from nexus import generate_physical_system
    from nexus import generate_qmcpack_input

    dia = generate_physical_system(
        units     = 'A',
        axes      = [[ 1.785,  1.785,  0.   ],
                     [ 0.   ,  1.785,  1.785],
                     [ 1.785,  0.   ,  1.785]],
        elem      = ['C','C'],
        pos       = [[ 0.    ,  0.    ,  0.    ],
                     [ 0.8925,  0.8925,  0.8925]],
        tiling    = [3,1,3], 
        kgrid     = (1,1,1), 
        kshift    = (0,0,0), 
        C         = 4
        )
  
  
    # test kp_index, band_index format (format="band")
    qmc_optical = generate_qmcpack_input(
        det_format     = 'old',
        spin_polarized = True,
        system         = dia,
        excitation     = ['up', '0 3 4 4'], #
        pseudos        = ['C.BFD.xml'],
        jastrows       = [],
        qmc            = 'vmc',
        )

    expect = '''<slaterdeterminant>
   <determinant id="updet" size="36">
      <occupation mode="excited" spindataset="0" pairs="1" format="band">             
0 3 4 4
       </occupation>
   </determinant>
   <determinant id="downdet" size="36">
      <occupation mode="ground" spindataset="1"/>
   </determinant>
</slaterdeterminant>'''.strip()

    text = qmc_optical.get('slaterdeterminant').write().strip()
    assert(text==expect)


    # test energy_index (format="energy")
    qmc_optical = generate_qmcpack_input(
        det_format     = 'old',
        spin_polarized = True,
        system         = dia,
        excitation     = ['up', '-35 36'], #
        pseudos        = ['C.BFD.xml'],
        jastrows       = [],
        qmc            = 'vmc',
        )

    expect = '''<slaterdeterminant>
   <determinant id="updet" size="36">
      <occupation mode="excited" spindataset="0" pairs="1" format="energy">             
-35 36
        </occupation>
   </determinant>
   <determinant id="downdet" size="36">
      <occupation mode="ground" spindataset="1"/>
   </determinant>
</slaterdeterminant>'''.strip()

    text = qmc_optical.get('slaterdeterminant').write().strip()
    assert(text==expect)

#end def test_excited_state



if versions.seekpath_available:
    def test_symbolic_excited_state():
        from nexus import generate_physical_system
        from nexus import generate_qmcpack_input

        dia = generate_physical_system(
            units     = 'A',
            axes      = [[ 1.785,  1.785,  0.   ],
                         [ 0.   ,  1.785,  1.785],
                         [ 1.785,  0.   ,  1.785]],
            elem      = ['C','C'],
            pos       = [[ 0.    ,  0.    ,  0.    ],
                         [ 0.8925,  0.8925,  0.8925]],
            use_prim  = True,    # Use SeeK-path library to identify prim cell
            tiling    = [2,1,2], 
            kgrid     = (1,1,1), 
            kshift    = (0,0,0), # Assumes we study transitions from Gamma. For non-gamma tilings, use kshift appropriately
            #C         = 4
            )

        qmc_optical = generate_qmcpack_input(
            det_format     = 'old',
            input_type     = 'basic',
            spin_polarized = True,
            system         = dia,
            excitation     = ['up', 'gamma vb x cb'], 
            jastrows       = [],
            qmc            = 'vmc',
            )

        expect = '''<slaterdeterminant>
   <determinant id="updet" size="24">
      <occupation mode="excited" spindataset="0" pairs="1" format="band">             
0 5 3 6
       </occupation>
   </determinant>
   <determinant id="downdet" size="24">
      <occupation mode="ground" spindataset="1"/>
   </determinant>
</slaterdeterminant>'''.strip()
        text = qmc_optical.get('slaterdeterminant').write().strip()
        assert(text==expect)


        qmc_optical = generate_qmcpack_input(
            det_format     = 'old',
            input_type     = 'basic',
            spin_polarized = True,
            system         = dia,
            excitation     = ['up', 'gamma vb-1 x cb'], 
            jastrows       = [],
            qmc            = 'vmc',
            )

        expect = '''<slaterdeterminant>
   <determinant id="updet" size="24">
      <occupation mode="excited" spindataset="0" pairs="1" format="band">             
0 4 3 6
       </occupation>
   </determinant>
   <determinant id="downdet" size="24">
      <occupation mode="ground" spindataset="1"/>
   </determinant>
</slaterdeterminant>'''.strip()
        text = qmc_optical.get('slaterdeterminant').write().strip()
        assert(text==expect)


        qmc_optical = generate_qmcpack_input(
            det_format     = 'old',
            input_type     = 'basic',
            spin_polarized = True,
            system         = dia,
            excitation     = ['up', 'gamma vb x cb+1'], 
            jastrows       = [],
            qmc            = 'vmc',
            )

        expect = '''<slaterdeterminant>
   <determinant id="updet" size="24">
      <occupation mode="excited" spindataset="0" pairs="1" format="band">             
0 5 3 7
       </occupation>
   </determinant>
   <determinant id="downdet" size="24">
      <occupation mode="ground" spindataset="1"/>
   </determinant>
</slaterdeterminant>'''.strip()
        text = qmc_optical.get('slaterdeterminant').write().strip()
        assert(text==expect)

    #end def test_symbolic_excited_state
#end if

