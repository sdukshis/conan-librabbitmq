from conans import ConanFile, CMake
import os

# This easily allows to copy the package in other user or channel
channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "filonovpv")

class TestLibrabbitmqConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "librabbitmq/0.8.1@%s/%s" % (username, channel)
    generators = "cmake"
    default_options = "librabbitmq:no_openssl=True"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.run(os.sep.join([".","bin", "test_librabbitmq"]))