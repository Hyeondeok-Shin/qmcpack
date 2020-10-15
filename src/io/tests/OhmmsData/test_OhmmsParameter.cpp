//////////////////////////////////////////////////////////////////////////////////////
// This file is distributed under the University of Illinois/NCSA Open Source License.
// See LICENSE file in top directory for details.
//
// Copyright (c) 2016 Jeongnim Kim and QMCPACK developers.
//
// File developed by: Mark Dewing, markdewing@gmail.com, University of Illinois at Urbana-Champaign
//
// File created by: Jeongnim Kim, jeongnim.kim@gmail.com, University of Illinois at Urbana-Champaign
//////////////////////////////////////////////////////////////////////////////////////


#include "catch.hpp"

#include "OhmmsData/Libxml2Doc.h"
#include "OhmmsData/OhmmsParameter.h"
#include <string>
#include <vector>

using std::string;
using std::vector;

TEST_CASE("OhmmsParameter", "[xml]")
{
  const char* content = " \
<simulation name=\"here \" electron=\"\" proton=\" \"> \
</simulation>";
  Libxml2Document doc;
  bool okay = doc.parseFromString(content);
  REQUIRE(okay == true);
  xmlNodePtr root = doc.getRoot();

  SECTION("String att exist non white space")
  {
    const char* att_name = "name";
    XMLAttrString att_input(root, att_name);
    REQUIRE(att_input == "here ");

    std::string str_value("qmcqmc");
    OhmmsParameter<std::string> param_str(str_value, att_name);
    std::istringstream input_stream(att_input);
    param_str.put(input_stream);
    REQUIRE(str_value == "here");
  }

  SECTION("String att exist but empty")
  {
    const char* att_name = "electron";
    XMLAttrString att_input(root, att_name);
    REQUIRE(att_input == "");

    std::string str_value("qmcqmc");
    OhmmsParameter<std::string> param_str(str_value, att_name);
    std::istringstream input_stream(att_input);
    REQUIRE_THROWS(param_str.put(input_stream));
  }

  SECTION("String att exist but with one space")
  {
    const char* att_name = "proton";
    XMLAttrString att_input(root, att_name);
    REQUIRE(att_input == " ");

    std::string str_value("qmcqmc");
    OhmmsParameter<std::string> param_str(str_value, att_name);
    std::istringstream input_stream(att_input);
    REQUIRE_THROWS(param_str.put(input_stream));
  }

  SECTION("String att non exist")
  {
    const char* att_name = "ion";
    XMLAttrString att_input(root, att_name);
    REQUIRE(att_input == "");

    std::string str_value("qmcqmc");
    OhmmsParameter<std::string> param_str(str_value, att_name);
    std::istringstream input_stream(att_input);
    param_str.put(input_stream);
    REQUIRE(str_value == "qmcqmc");
  }

  // testing integer
  //int int_value = 12;
  //OhmmsParameter<int> param_int(int_value, "simulation");
  //XMLAttrString name(root, "name");

  //std::istringstream stream((const char*)(att->children->content));
  //param_int.put()
}
