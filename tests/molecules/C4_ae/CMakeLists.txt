IF (NOT QMC_CUDA)
 IF (NOT QMC_COMPLEX)

#E =  -150.95531020041986

  LIST(APPEND C4_SD_AE_NO_SHORT "totenergy" "-150.95979067 0.07502463")

  QMC_RUN_AND_CHECK(short-C4_sd-ae-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-SD-C4_AE_Mol_NO
                    qmc_short-SD-C4_AE_Mol_NO.in.xml 
                    1 16
                    TRUE
                    0 C4_SD_AE_NO_SHORT # VMC
                    )

  LIST(APPEND C4_SD_AE_NO_LONG "totenergy" "-150.95979067 0.00684878")

  QMC_RUN_AND_CHECK(long-C4_sd-ae-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-SD-C4_AE_Mol_NO
                    qmc_long-SD-C4_AE_Mol_NO.in.xml
                    1 16
                    TRUE
                    0 C4_SD_AE_NO_LONG # VMC
                    )

#Nb_Det = 160
#Ground:
#E               =   -151.08986108933223
#Vnn             =    56.960598881874070
#Ven             =   -464.83401896934589
#Vee             =    106.77210949007733
#T               =    150.01144950806227

#Excited:
#E               =   -150.93124043303607
#Vnn             =    56.960598881874070
#Ven             =   -465.62023598802489
#Vee             =    107.09690302643341
#T               =    150.63149364668132

  LIST(APPEND C4_MD_AE_GROUND_NO_SHORT "kinetic" "150.62502805 3.05983967")
  LIST(APPEND C4_MD_AE_GROUND_NO_SHORT "totenergy" "-151.10450294 0.06270194")
  LIST(APPEND C4_MD_AE_GROUND_NO_SHORT "potential" "-301.72953099 3.05940359")
  LIST(APPEND C4_MD_AE_GROUND_NO_SHORT "eeenergy" "106.76696948 0.09266910")
  LIST(APPEND C4_MD_AE_GROUND_NO_SHORT "ionion" "56.96059899 0.000001")
  LIST(APPEND C4_MD_AE_GROUND_NO_SHORT "samples" "128000 0.0")

  QMC_RUN_AND_CHECK(short-C4_md-ae-ground-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-MD-C4_AE_Mol_Ground_NO
                    qmc_short-MD-C4_AE_Mol_Ground_NO.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_GROUND_NO_SHORT # VMC
                    )


  LIST(APPEND C4_MD_AE_GROUND_NO_LONG "kinetic" "150.62502805 0.68420095")
  LIST(APPEND C4_MD_AE_GROUND_NO_LONG "totenergy" "-151.10450294 0.01402058")
  LIST(APPEND C4_MD_AE_GROUND_NO_LONG "potential" "-301.72953099 0.68410344")
  LIST(APPEND C4_MD_AE_GROUND_NO_LONG "eeenergy" "106.76696948 0.02072144")
  LIST(APPEND C4_MD_AE_GROUND_NO_LONG "ionion" "56.96059899 0.000001")
  LIST(APPEND C4_MD_AE_GROUND_NO_LONG "samples" "2560000 0.0")

  QMC_RUN_AND_CHECK(long-C4_md-ae-ground-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-MD-C4_AE_Mol_Ground_NO
                    qmc_long-MD-C4_AE_Mol_Ground_NO.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_GROUND_NO_LONG # VMC
                    )

  LIST(APPEND C4_MD_AE_EXCITED_NO_SHORT "kinetic" "150.43338165 2.93306038")
  LIST(APPEND C4_MD_AE_EXCITED_NO_SHORT "totenergy" "-150.91086912 0.07676144")
  LIST(APPEND C4_MD_AE_EXCITED_NO_SHORT "potential" "-301.34425077 2.92544943")
  LIST(APPEND C4_MD_AE_EXCITED_NO_SHORT "eeenergy" "107.13372653 0.11219028")
  LIST(APPEND C4_MD_AE_EXCITED_NO_SHORT "ionion" "56.96059899 0.000001")
  LIST(APPEND C4_MD_AE_EXCITED_NO_SHORT "samples" "128000 0.0")

  QMC_RUN_AND_CHECK(short-C4_md-ae-excited-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-MD-C4_AE_Mol_Excited_NO
                    qmc_short-MD-C4_AE_Mol_Excited_NO.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_EXCITED_NO_SHORT # VMC
                    )


  LIST(APPEND C4_MD_AE_EXCITED_NO_LONG "kinetic" "150.43338165 0.65585224")
  LIST(APPEND C4_MD_AE_EXCITED_NO_LONG "totenergy" "-150.91086912 0.01716438")
  LIST(APPEND C4_MD_AE_EXCITED_NO_LONG "potential" "-301.34425077 0.65415038")
  LIST(APPEND C4_MD_AE_EXCITED_NO_LONG "eeenergy" "107.13372653 0.02508651")
  LIST(APPEND C4_MD_AE_EXCITED_NO_LONG "ionion" "56.96059899 0.000001")
  LIST(APPEND C4_MD_AE_EXCITED_NO_LONG "samples" "2560000 0.0")

  QMC_RUN_AND_CHECK(long-C4_md-ae-excited-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-MD-C4_AE_Mol_Excited_NO
                    qmc_long-MD-C4_AE_Mol_Excited_NO.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_EXCITED_NO_LONG # VMC
                    )


# E = -150.95837457762536

  LIST(APPEND C4_SD_AE_PYSCF_SHORT "totenergy" "-150.96861932 0.07808201")

  QMC_RUN_AND_CHECK(short-C4_sd-ae-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-SD-C4_AE_Mol_pyscf
                    qmc_short-SD-C4_AE_Mol_pyscf.in.xml
                    1 16
                    TRUE
                    0 C4_SD_AE_PYSCF_SHORT # VMC
                    )


  LIST(APPEND C4_SD_AE_PYSCF_LONG "totenergy" "-150.96861932 0.00712788")

  QMC_RUN_AND_CHECK(long-C4_sd-ae-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-SD-C4_AE_Mol_pyscf
                    qmc_long-SD-C4_AE_Mol_pyscf.in.xml
                    1 16
                    TRUE
                    0 C4_SD_AE_PYSCF_LONG # VMC
                    )


#Nb_Det = 213
#Ground:
#E               =   -151.05927585983179
#Vnn             =    56.960598881874070
#Ven             =   -464.01077697638391
#Vee             =    106.34761975170790
#T               =    149.64328248297016

#Excited:
#E               =   -150.88919835469994
#Vnn             =    56.960598881874070
#Ven             =   -463.19702130387998
#Vee             =    106.04380266024245
#T               =    149.30342140706352

  LIST(APPEND C4_MD_AE_GROUND_PYSCF_SHORT "kinetic" "149.28465371 3.00472176")
  LIST(APPEND C4_MD_AE_GROUND_PYSCF_SHORT "totenergy" "-151.06336670 0.07104283")
  LIST(APPEND C4_MD_AE_GROUND_PYSCF_SHORT "potential" "-300.34802042 2.99260965")
  LIST(APPEND C4_MD_AE_GROUND_PYSCF_SHORT "eeenergy" "106.34306716 0.09656683")
  LIST(APPEND C4_MD_AE_GROUND_PYSCF_SHORT "ionion" "56.96059899 0.000001")
  QMC_RUN_AND_CHECK(short-C4_md-ae-ground-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-MD-C4_AE_Mol_Ground_pyscf
                    qmc_short-MD-C4_AE_Mol_Ground_pyscf.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_GROUND_PYSCF_SHORT # VMC                    
                   )

  LIST(APPEND C4_MD_AE_GROUND_PYSCF_LONG "kinetic" "149.28465371 0.67187621")
  LIST(APPEND C4_MD_AE_GROUND_PYSCF_LONG "totenergy" "-151.06336670 0.01588566")
  LIST(APPEND C4_MD_AE_GROUND_PYSCF_LONG "potential" "-300.34802042 0.66916786")
  LIST(APPEND C4_MD_AE_GROUND_PYSCF_LONG "eeenergy" "106.34306716 0.02159300")
  LIST(APPEND C4_MD_AE_GROUND_PYSCF_LONG "ionion" "56.96059899 0.000001")
  QMC_RUN_AND_CHECK(long-C4_md-ae-ground-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-MD-C4_AE_Mol_Ground_pyscf
                    qmc_long-MD-C4_AE_Mol_Ground_pyscf.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_GROUND_PYSCF_LONG # VMC
                   )


  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_SHORT "kinetic" "148.67622775 2.69957204") 
  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_SHORT "totenergy" "-150.87787794 0.06865167") 
  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_SHORT "potential" "-299.55410569 2.70119471")
  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_SHORT "eeenergy" "106.07213568 0.09271722") 
  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_SHORT "ionion" "56.96059899 0.000001")

  QMC_RUN_AND_CHECK(short-C4_md-ae-excited-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-MD-C4_AE_Mol_Excited_pyscf
                    qmc_short-MD-C4_AE_Mol_Excited_pyscf.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_EXCITED_PYSCF_SHORT # VMC
                   )


  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_LONG "kinetic" "148.67622775 0.60364266")
  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_LONG "totenergy" "-150.87787794 0.01535098")
  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_LONG "potential" "-299.55410569 0.60400550")
  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_LONG "eeenergy" "106.07213568 0.02073220")
  LIST(APPEND C4_MD_AE_EXCITED_PYSCF_LONG "ionion" "56.96059899 0.000001")

  QMC_RUN_AND_CHECK(long-C4_md-ae-excited-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-MD-C4_AE_Mol_Excited_pyscf
                    qmc_long-MD-C4_AE_Mol_Excited_pyscf.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_EXCITED_PYSCF_LONG # VMC
                   )


# -150.95914112726956

  LIST(APPEND C4_SD_AE_QP_SHORT "totenergy" "-150.96684038 0.08123459")

  QMC_RUN_AND_CHECK(short-C4_sd-ae-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-SD-C4_AE_Mol_QP
                    qmc_short-SD-C4_AE_Mol_QP.in.xml
                    1 16
                    TRUE
                    0 C4_SD_AE_QP_SHORT # VMC
                    )


  LIST(APPEND C4_SD_AE_QP_LONG "totenergy" "-150.96684038 0.00741567")

  QMC_RUN_AND_CHECK(long-C4_sd-ae-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-SD-C4_AE_Mol_QP
                    qmc_long-SD-C4_AE_Mol_QP.in.xml
                    1 16
                    TRUE
                    0 C4_SD_AE_QP_LONG # VMC
                    )


#Nb_Det = 211
#Ground:
#E               =   -151.05736895837109
#Vnn             =    56.960598986007938
#Ven             =   -464.01242694605406
#Vee             =    106.35022537160214
#T               =    149.64423363007290


#Excited:
#E               =   -150.88866382584013
#Vnn             =    56.960598986007938
#Ven             =   -463.18948426388619
#Vee             =    106.03958987195335
#T               =    149.30063158008477


  LIST(APPEND C4_MD_AE_GROUND_QP_SHORT "kinetic" "149.23349817 2.78532373")
  LIST(APPEND C4_MD_AE_GROUND_QP_SHORT "totenergy" "-151.05662477 0.07087186")
  LIST(APPEND C4_MD_AE_GROUND_QP_SHORT "potential" "-300.29012294 2.78052732")
  LIST(APPEND C4_MD_AE_GROUND_QP_SHORT "eeenergy" "106.34927122 0.09558193")
  LIST(APPEND C4_MD_AE_GROUND_QP_SHORT "ionion" "56.96059899 0.000001")

  QMC_RUN_AND_CHECK(short-C4_md-ae-ground-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-MD-C4_AE_Mol_Ground_QP
                    qmc_short-MD-C4_AE_Mol_Ground_QP.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_GROUND_QP_SHORT # VMC
                   )


  LIST(APPEND C4_MD_AE_GROUND_QP_LONG "kinetic" "149.23349817 0.62281732")
  LIST(APPEND C4_MD_AE_GROUND_QP_LONG "totenergy" "-151.05662477 0.01584743")
  LIST(APPEND C4_MD_AE_GROUND_QP_LONG "potential" "-300.29012294 0.62174481")
  LIST(APPEND C4_MD_AE_GROUND_QP_LONG "eeenergy" "106.34927122 0.02137277")
  LIST(APPEND C4_MD_AE_GROUND_QP_LONG "ionion" "56.96059899 0.000001")

  QMC_RUN_AND_CHECK(long-C4_md-ae-ground-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-MD-C4_AE_Mol_Ground_QP
                    qmc_long-MD-C4_AE_Mol_Ground_QP.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_GROUND_QP_LONG # VMC
                   )

  LIST(APPEND C4_MD_AE_EXICTED_QP_SHORT "kinetic" "150.14151034 3.05156850")
  LIST(APPEND C4_MD_AE_EXCITED_QP_SHORT "totenergy" "-150.89030273 0.06996075")
  LIST(APPEND C4_MD_AE_EXCITED_QP_SHORT "potential" "-301.03181306 3.04428187")
  LIST(APPEND C4_MD_AE_EXCITED_QP_SHORT "eeenergy" "106.07206355 0.10266535")
  LIST(APPEND C4_MD_AE_EXCITED_QP_SHORT "ionion" "56.96059899 0.000001")

  QMC_RUN_AND_CHECK(short-C4_md-ae-excited-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_short-MD-C4_AE_Mol_Excited_QP
                    qmc_short-MD-C4_AE_Mol_Excited_QP.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_EXCITED_QP_SHORT # VMC
                   )


  LIST(APPEND C4_MD_AE_EXICTED_QP_LONG "kinetic" "150.14151034 0.68235146")
  LIST(APPEND C4_MD_AE_EXCITED_QP_LONG "totenergy" "-150.89030273 0.01564370")
  LIST(APPEND C4_MD_AE_EXCITED_QP_LONG "potential" "-301.03181306 0.68072212")
  LIST(APPEND C4_MD_AE_EXCITED_QP_LONG "eeenergy" "106.07206355 0.02295667")
  LIST(APPEND C4_MD_AE_EXCITED_QP_LONG "ionion" "56.96059899 0.000001")

  QMC_RUN_AND_CHECK(long-C4_md-ae-excited-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    qmc_long-MD-C4_AE_Mol_Excited_QP
                    qmc_long-MD-C4_AE_Mol_Excited_QP.in.xml
                    1 16
                    TRUE
                    0 C4_MD_AE_EXCITED_QP_LONG # VMC
                   )


#Deterministic tests

  LIST(APPEND DET_C4_SD_AE_NO_SHORT "kinetic" "40.88568798 0.00001") 
  LIST(APPEND DET_C4_SD_AE_NO_SHORT "totenergy" "-146.21104723 0.00001") 
  LIST(APPEND DET_C4_SD_AE_NO_SHORT "potential" "-187.09673521 0.00001")
  LIST(APPEND DET_C4_SD_AE_NO_SHORT "eeenergy" "99.68606745 0.00001")
  LIST(APPEND DET_C4_SD_AE_NO_SHORT "ionion" "56.96059899 0.00001")
  LIST(APPEND DET_C4_SD_AE_NO_SHORT "samples" "9 0.0") 
  QMC_RUN_AND_CHECK(deterministic-C4_sd-ae-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-SD-C4_AE_Mol_NO
                    det_qmc_short-SD-C4_AE_Mol_NO.in.xml
                    1 1
                    TRUE
                    0 DET_C4_SD_AE_NO_SHORT # VMC
                    )


  LIST(APPEND DET_C4_MD_AE_GROUND_NO_SHORT "kinetic" "81.37875523 0.00001") 
  LIST(APPEND DET_C4_MD_AE_GROUND_NO_SHORT "totenergy" "-147.35211603 0.00001") 
  LIST(APPEND DET_C4_MD_AE_GROUND_NO_SHORT "potential" "-228.73087126 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_NO_SHORT "eeenergy" "94.66385499 0.00001") 
  LIST(APPEND DET_C4_MD_AE_GROUND_NO_SHORT "ionion" "56.96059899 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_NO_SHORT "samples" "9 0.0") 
  QMC_RUN_AND_CHECK(deterministic-C4_md-ae-ground-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-MD-C4_AE_Mol_Ground_NO
                    det_qmc_short-MD-C4_AE_Mol_Ground_NO.in.xml
                    1 1
                    TRUE
                    0 DET_C4_MD_AE_GROUND_NO_SHORT # VMC
                    )


  LIST(APPEND DET_C4_MD_AE_EXCITED_NO_SHORT "kinetic" "120.73710114 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_NO_SHORT "totenergy" "-139.80104570 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_NO_SHORT "potential" "-260.53814684 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_NO_SHORT "eeenergy" "114.94712080 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_NO_SHORT "ionion" "56.96059899 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_NO_SHORT "samples" "9 0.0")
  QMC_RUN_AND_CHECK(deterministic-C4_md-ae-excited-no-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-MD-C4_AE_Mol_Excited_NO
                    det_qmc_short-MD-C4_AE_Mol_Excited_NO.in.xml
                    1 1
                    TRUE
                    0 DET_C4_MD_AE_EXCITED_NO_SHORT # VMC
                    )


  LIST(APPEND DET_C4_SD_AE_PYSCF_SHORT "kinetic" "30.86817337 0.00001")
  LIST(APPEND DET_C4_SD_AE_PYSCF_SHORT "totenergy" "-148.23557897 0.00001")
  LIST(APPEND DET_C4_SD_AE_PYSCF_SHORT "potential" "-179.10375234 0.00001")
  LIST(APPEND DET_C4_SD_AE_PYSCF_SHORT "eeenergy" "104.75324877 0.00001")
  LIST(APPEND DET_C4_SD_AE_PYSCF_SHORT "ionion" "56.96059888 0.00001")
  LIST(APPEND DET_C4_SD_AE_PYSCF_SHORT "samples" "9 0.0")
  QMC_RUN_AND_CHECK(deterministic-C4_sd-ae-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-SD-C4_AE_Mol_pyscf
                    det_qmc_short-SD-C4_AE_Mol_pyscf.in.xml
                    1 1
                    TRUE
                    0 DET_C4_SD_AE_PYSCF_SHORT # VMC
                    )


  LIST(APPEND DET_C4_MD_AE_GROUND_PYSCF_SHORT "kinetic" "45.21132325 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_PYSCF_SHORT "totenergy" "-152.67877846 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_PYSCF_SHORT "potential" "-197.89010170 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_PYSCF_SHORT "eeenergy" "98.26527092 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_PYSCF_SHORT "ionion" "56.96059899 0.00001")

  QMC_RUN_AND_CHECK(deterministic-C4_md-ae-ground-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-MD-C4_AE_Mol_Ground_pyscf
                    det_qmc_short-MD-C4_AE_Mol_Ground_pyscf.in.xml
                    1 1
                    TRUE
                    0 DET_C4_MD_AE_GROUND_PYSCF_SHORT # VMC
                   )


  LIST(APPEND DET_C4_MD_AE_EXCITED_PYSCF_SHORT "kinetic" "22.49757293 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_PYSCF_SHORT "totenergy" "-145.22397858 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_PYSCF_SHORT "potential" "-167.72155151 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_PYSCF_SHORT "eeenergy" "101.91736704 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_PYSCF_SHORT "ionion" "56.96059899 0.00001")

  QMC_RUN_AND_CHECK(deterministic-C4_md-ae-excited-pyscf-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-MD-C4_AE_Mol_Excited_pyscf
                    det_qmc_short-MD-C4_AE_Mol_Excited_pyscf.in.xml
                    1 1
                    TRUE
                    0 DET_C4_MD_AE_EXCITED_PYSCF_SHORT # VMC
                   )


  LIST(APPEND DET_C4_SD_AE_QP_SHORT "kinetic" "54.11526393 0.00001")
  LIST(APPEND DET_C4_SD_AE_QP_SHORT "totenergy" "-152.43823035 0.00001")
  LIST(APPEND DET_C4_SD_AE_QP_SHORT "potential" "-206.55349428 0.00001")
  LIST(APPEND DET_C4_SD_AE_QP_SHORT "eeenergy" "99.57907161 0.00001")
  LIST(APPEND DET_C4_SD_AE_QP_SHORT "ionion" "56.96059899 0.00001")
  LIST(APPEND DET_C4_SD_AE_QP_SHORT "samples" "9 0.0")

  QMC_RUN_AND_CHECK(deterministic-C4_sd-ae-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-SD-C4_AE_Mol_QP
                    det_qmc_short-SD-C4_AE_Mol_QP.in.xml
                    1 1
                    TRUE
                    0 DET_C4_SD_AE_QP_SHORT # VMC
                    )



  LIST(APPEND DET_C4_MD_AE_GROUND_QP_SHORT "kinetic" "70.64698241 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_QP_SHORT "totenergy" "-154.62718031 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_QP_SHORT "potential" "-225.27416271 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_QP_SHORT "eeenergy" "105.93504749 0.00001")
  LIST(APPEND DET_C4_MD_AE_GROUND_QP_SHORT "ionion" "56.96059899 0.00001")
  QMC_RUN_AND_CHECK(deterministic-C4_md-ae-ground-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-MD-C4_AE_Mol_Ground_QP
                    det_qmc_short-MD-C4_AE_Mol_Ground_QP.in.xml
                    1 1
                    TRUE
                    0 DET_C4_MD_AE_GROUND_QP_SHORT # VMC
                   )


  LIST(APPEND DET_C4_MD_AE_EXICTED_QP_SHORT "kinetic" "-4.57501459 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_QP_SHORT "totenergy" "-147.01870207 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_QP_SHORT "potential" "-142.44368748 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_QP_SHORT "eeenergy" "95.13749252 0.00001")
  LIST(APPEND DET_C4_MD_AE_EXCITED_QP_SHORT "ionion" "56.96059899 0.00001")
  QMC_RUN_AND_CHECK(deterministic-C4_md-ae-excited-qp-vmc
                    "${CMAKE_SOURCE_DIR}/tests/molecules/C4_ae"
                    det_qmc_short-MD-C4_AE_Mol_Excited_QP
                    det_qmc_short-MD-C4_AE_Mol_Excited_QP.in.xml
                    1 1
                    TRUE
                    0 DET_C4_MD_AE_EXCITED_QP_SHORT # VMC
                   )



 ELSE()
    MESSAGE_VERBOSE("Skipping C2_MSD_Excited tests because Pure real WF are not supported by complex build (QMC_COMPLEX=1)")
 ENDIF()
ELSE()
    MESSAGE_VERBOSE("Skipping C2_MSD_Excited tests because gaussian basis sets are not supported by CUDA build (QMC_CUDA=1)")
ENDIF()
