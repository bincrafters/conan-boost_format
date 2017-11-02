from conans import ConanFile, tools
import os

class BoostFormatConan(ConanFile):
    name = "Boost.Format"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-format"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["format"]
    requires =  "Boost.Assert/1.65.1@bincrafters/testing", \
                      "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Optional/1.65.1@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
                      "Boost.Utility/1.65.1@bincrafters/testing"

                      #assert1 config0 optional5 smart_ptr4 throw_exception2 utility5

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()