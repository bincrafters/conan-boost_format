#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostFormatConan(base.BoostBaseConan):
    name = "boost_format"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_format"
    lib_short_names = ["format"]
    header_only_libs = ["format"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_optional",
        "boost_smart_ptr",
        "boost_throw_exception",
        "boost_utility"
    ]
