if(NOT QMC_CUDA)

  list(APPEND HE2_SP_SCALARS "totenergy" "-2.32676861 0.0863")
  list(APPEND HE2_SP_SCALARS "kinetic" "16.23198428 0.1117")
  list(APPEND HE2_SP_SCALARS "potential" "-18.55875289 0.1136")
  list(APPEND HE2_SP_SCALARS "eeenergy" "4.59673345 0.0174")
  list(APPEND HE2_SP_SCALARS "ionion" "0.86420131 0.0001")
  list(APPEND HE2_SP_SCALARS "samples" "16000 0.0")

  qmc_run_and_check(
    short-he2_1x1x1_ae-vmc_gaussian-sp-sph_noj
    "${qmcpack_SOURCE_DIR}/tests/solids/he2_1x1x1_ae"
    he2_sp_sph
    he2_sp_sph.qmc.in-wfnoj.xml
    1
    16
    TRUE
    0
    HE2_SP_SCALARS # VMC
  )

  list(APPEND HE2_SD_SCALARS "totenergy" "-2.32942007 0.0835")
  list(APPEND HE2_SD_SCALARS "kinetic" "16.21547981 0.1067")
  list(APPEND HE2_SD_SCALARS "potential" "-18.54489989 0.1189")
  list(APPEND HE2_SD_SCALARS "eeenergy" "4.59377532 0.0184")
  list(APPEND HE2_SD_SCALARS "ionion" "0.86420131 0.0001")
  list(APPEND HE2_SD_SCALARS "samples" "16000 0.0")

  qmc_run_and_check(
   short-he2_1x1x1_ae-vmc_gaussian-sd-sph_noj
   "${qmcpack_SOURCE_DIR}/tests/solids/he2_1x1x1_ae"
   he2_sd_sph
   he2_sd_sph.qmc.in-wfnoj.xml
   1
   16
   TRUE
   0
   HE2_SP_SCALARS # VMC
  )

else()
  message(VERBOSE "Skipping Periodic LCAO as not supported by CUDA build (QMC_CUDA=1)")
endif()
