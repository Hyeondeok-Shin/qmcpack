//////////////////////////////////////////////////////////////////////////////////////
// This file is distributed under the University of Illinois/NCSA Open Source License.
// See LICENSE file in top directory for details.
//
// Copyright (c) 2016 Jeongnim Kim and QMCPACK developers.
//
// File developed by:
//
// File created by: Jeongnim Kim, jeongnim.kim@intel.com, Intel Corp.
//////////////////////////////////////////////////////////////////////////////////////


#include "QMCWaveFunctions/BsplineFactory/createBsplineReader.h"
#include "CPU/e2iphi.h"
#include "CPU/SIMD/vmath.hpp"
#include "Utilities/ProgressReportEngine.h"
#include "QMCWaveFunctions/EinsplineSetBuilder.h"
#include "QMCWaveFunctions/BsplineFactory/BsplineSet.h"
#include "QMCWaveFunctions/BsplineFactory/SplineC2R.h"
#include "QMCWaveFunctions/BsplineFactory/SplineC2C.h"
#if defined(ENABLE_OFFLOAD)
#include "QMCWaveFunctions/BsplineFactory/SplineC2ROMPTarget.h"
#include "QMCWaveFunctions/BsplineFactory/SplineC2COMPTarget.h"
#endif
#include "QMCWaveFunctions/BsplineFactory/HybridRepCplx.h"
#include <fftw3.h>
#include "QMCWaveFunctions/einspline_helper.hpp"
#include "QMCWaveFunctions/BsplineFactory/BsplineReaderBase.h"
#include "QMCWaveFunctions/BsplineFactory/SplineSetReader.h"
#include "QMCWaveFunctions/BsplineFactory/HybridRepSetReader.h"

namespace qmcplusplus
{
BsplineReaderBase* createBsplineComplexDouble(EinsplineSetBuilder* e, bool hybrid_rep, const std::string& useGPU)
{
  typedef OHMMS_PRECISION RealType;
  BsplineReaderBase* aReader = nullptr;

#if defined(QMC_COMPLEX)
  app_summary() << "    Using complex valued spline SPOs with complex double precision storage (C2C)." << std::endl;
#if defined(ENABLE_OFFLOAD)
  if (useGPU == "yes")
  {
    if (hybrid_rep)
    {
      app_summary() << "OpenMP offload has not been implemented to support hybrid orbital representation!"
                    << " Running on CPU." << std::endl;
      app_summary() << "    Using hybrid orbital representation." << std::endl;
      aReader = new HybridRepSetReader<HybridRepCplx<SplineC2C<double>>>(e);
    }
    else
    {
      app_summary() << "    Running on an accelerator via OpenMP offload." << std::endl;
      aReader = new SplineSetReader<SplineC2COMPTarget<double>>(e);
    }
  }
  else
#endif
  {
    app_summary() << "    Running on CPU." << std::endl;
    if (hybrid_rep)
    {
      app_summary() << "    Using hybrid orbital representation." << std::endl;
      aReader = new HybridRepSetReader<HybridRepCplx<SplineC2C<double>>>(e);
    }
    else
      aReader = new SplineSetReader<SplineC2C<double>>(e);
  }
#else //QMC_COMPLEX
  app_summary() << "    Using real valued spline SPOs with complex double precision storage (C2R)." << std::endl;
#if defined(ENABLE_OFFLOAD)
  if (useGPU == "yes")
  {
    if (hybrid_rep)
    {
      app_summary() << "OpenMP offload has not been implemented to support hybrid orbital representation!"
                    << " Running on CPU." << std::endl;
      app_summary() << "    Using hybrid orbital representation." << std::endl;
      aReader = new HybridRepSetReader<HybridRepCplx<SplineC2R<double>>>(e);
    }
    else
    {
      app_summary() << "    Running on an accelerator via OpenMP offload." << std::endl;
      aReader = new SplineSetReader<SplineC2ROMPTarget<double>>(e);
    }
  }
  else
#endif
  {
    app_summary() << "    Running on CPU." << std::endl;
    if (hybrid_rep)
    {
      app_summary() << "    Using hybrid orbital representation." << std::endl;
      aReader = new HybridRepSetReader<HybridRepCplx<SplineC2R<double>>>(e);
    }
    else
      aReader = new SplineSetReader<SplineC2R<double>>(e);
  }
#endif

  return aReader;
}
} // namespace qmcplusplus
