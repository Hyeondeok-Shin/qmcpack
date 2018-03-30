//////////////////////////////////////////////////////////////////////////////////////
// This file is distributed under the University of Illinois/NCSA Open Source License.
// See LICENSE file in top directory for details.
//
// Copyright (c) 2018 Jeongnim Kim and QMCPACK developers.
//
// File developed by: Mark Dewing, mdewing@anl.gov, Argonne National Laboratory
//
// File created by: Mark Dewing, mdewing@anl.gov, Argonne National Laboratory
//////////////////////////////////////////////////////////////////////////////////////


#define CATCH_CONFIG_MAIN
#include "catch.hpp"

#include "OhmmsPETE/OhmmsArray.h"
#include "spline2/MultiBspline.hpp"

namespace qmcplusplus
{

// Values from gen_prefactors.py
template<typename T>
void test_spline_bounds()
{
  SplineBound<T> sb;
  T x = 2.2;
  T dx;
  int ind;
  int ng=10;
  sb.get(x, dx, ind, ng);
  REQUIRE(dx == Approx(0.2));
  REQUIRE(ind == 2);

  // check clamping to a maximum index value
  x = 11.5;
  sb.get(x, dx, ind, ng);
  REQUIRE(dx == Approx(0.5));
  REQUIRE(ind == 10);

  // check clamping to a zero index value
  x = -1.3;
  sb.get(x, dx, ind, ng);
  REQUIRE(dx == Approx(-0.3));
  REQUIRE(ind == 0);

}

TEST_CASE("SplineBound double","[spline2]")
{
  test_spline_bounds<double>();
}


TEST_CASE("SplineBound float","[spline2]")
{
  test_spline_bounds<float>();
}


TEST_CASE("SymTrace","[spline2]")
{

  double h00 = 1;
  double h01 = 2;
  double h02 = 3;
  double h11 = 4.4;
  double h12 = 1.1;
  double h22 = 0.9;

  double gg[6] = {0.1, 1.6, 1.2, 2.3, 9.4, 2.3};

  double tr = SymTrace(h00, h01, h02, h11, h12, h22, gg);
  REQUIRE(tr == Approx(29.43));
}

// Values from gen_prefactors.py
template<typename T>
void test_prefactors()
{
  MultiBsplineData<T> bd;
  T a[4];
  T tx = 0.1;
  bd.compute_prefactors(a, tx);

  REQUIRE(a[0] == Approx(0.1215));
  REQUIRE(a[1] == Approx(0.657167));
  REQUIRE(a[2] == Approx(0.221167));
  REQUIRE(a[3] == Approx(0.000166667));

  T da[4];
  T d2a[4];
  tx = 0.8;

  bd.compute_prefactors(a, da, d2a, tx);
  REQUIRE(a[0] == Approx(0.00133333));
  REQUIRE(da[0] == Approx(-0.02));
  REQUIRE(d2a[0] == Approx(0.2));
  REQUIRE(a[1] == Approx(0.282667));
  REQUIRE(da[1] == Approx(-0.64));
  REQUIRE(d2a[1] == Approx(0.4));
  REQUIRE(a[2] == Approx(0.630667));
  REQUIRE(da[2] == Approx(0.34));
  REQUIRE(d2a[2] == Approx(-1.4));
  REQUIRE(a[3] == Approx(0.0853333));
  REQUIRE(da[3] == Approx(0.32));
  REQUIRE(d2a[3] == Approx(0.8));
}

TEST_CASE("double prefactors","[spline2]")
{
  test_prefactors<double>();
}

TEST_CASE("float prefactors","[spline2]")
{
  test_prefactors<float>();
}


// See gen_bspline_values.py

template<typename T>
void test_splines()
{
  MultiBspline<T> bs;

  int num_splines = 1;
  BCtype_d bc[3];
  Ugrid grid[3];

  // copied from einspline/tests/test_3d.cpp
  int N = 5;

  grid[0].start = 0.0;
  grid[0].end = 1.0;
  grid[0].num = N;

  grid[1].start = 0.0;
  grid[1].end = 1.0;
  grid[1].num = N;

  grid[2].start = 0.0;
  grid[2].end = 1.0;
  grid[2].num = N;

  double delta = (grid[0].end - grid[0].start)/grid[0].num;

  bc[0].lCode = PERIODIC;
  bc[0].rCode = PERIODIC;
  bc[0].lVal= 0.0;
  bc[0].rVal= 0.0;
  bc[1].lCode = PERIODIC;
  bc[1].rCode = PERIODIC;
  bc[1].lVal= 0.0;
  bc[1].rVal= 0.0;
  bc[2].lCode = PERIODIC;
  bc[2].rCode = PERIODIC;
  bc[2].lVal= 0.0;
  bc[2].rVal= 0.0;

  double tpi = 2*M_PI;

  Array<T, 3> data(N, N, N);
  // Generate the data in double precision regardless of the target spline precision
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < N; k++) {
        double x = delta*i;
        double y = delta*j;
        double z = delta*k;
        data(i,j,k) = std::sin(tpi*x) + std::sin(3*tpi*y) + std::sin(4*tpi*z);
      }
    }
  }


  bs.create(grid, bc, num_splines);

  REQUIRE(bs.num_splines() == 1);

  bs.set(0, data);

  Array<T, 1> v(1);
  TinyVector<T, 3> pos = {0.0, 0.0, 0.0};
  bs.evaluate(pos, v);
  REQUIRE(v(0) == Approx(0.0));

  Array<T, 2> dv(1,3);  // 3 - ndim
  Array<T, 2> hess(1, 6); // 6 - number of unique hessian components
  bs.evaluate_vgh(pos, v, dv, hess);
  REQUIRE(dv(0,0) == Approx(    6.178320809));
  REQUIRE(dv(0,1) == Approx(   -7.402942564));
  REQUIRE(dv(0,2) == Approx(   -6.178320809));


  for (int i = 0; i < 6; i++) {
    REQUIRE(hess(0,i) == Approx(0.0));
  }

  pos = {0.1, 0.2, 0.3};
  bs.evaluate(pos, v);

  REQUIRE(v(0) == Approx(  -0.9476393279));

  bs.evaluate_vgh(pos, v, dv, hess);

  REQUIRE(v(0) == Approx(  -0.9476393279));
  REQUIRE(dv(0,0) == Approx(    5.111042137));
  REQUIRE(dv(0,1) == Approx(    5.989106342));
  REQUIRE(dv(0,2) == Approx(    1.952244379));
  REQUIRE(hess(0, 0) == Approx(   -21.34557341));
  REQUIRE(hess(0, 1) == Approx(0.0));
  REQUIRE(hess(0, 2) == Approx(0.0));
  REQUIRE(hess(0, 3) == Approx(    133.9204891));
  REQUIRE(hess(0, 4) == Approx(0.0));
  REQUIRE(hess(0, 5) == Approx(    34.53786329));

  Array<T, 1> lap(1);
  bs.evaluate_vgl(pos, v, dv, lap);
  REQUIRE(v(0) == Approx(  -0.9476393279));
  REQUIRE(dv(0,0) == Approx(    5.111042137));
  REQUIRE(dv(0,1) == Approx(    5.989106342));
  REQUIRE(dv(0,2) == Approx(    1.952244379));
  REQUIRE(lap(0) == Approx(    147.1127789));

}

TEST_CASE("MultiBspline periodic double","[spline2]")
{
  test_splines<double>();
}

TEST_CASE("MultiBspline periodic float","[spline2]")
{
  test_splines<float>();
}
}
