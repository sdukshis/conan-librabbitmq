from conans import ConanFile, CMake
import os

class LibrabbitmqConan(ConanFile):
    url = "https://github.com/alanxz/rabbitmq-c"
    license = "https://github.com/alanxz/rabbitmq-c/blob/master/LICENSE-MIT"
    name = "librabbitmq"
    version = "0.8.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "no_openssl": [True, False],
    }
    default_options = "no_openssl=False"
    counter_config = 0

    def source(self):
        self.run("git clone --depth 50 https://github.com/alanxz/rabbitmq-c.git")

    def config(self):
        self.counter_config += 1
        if not self.options.no_openssl:
            if self.counter_config == 2:
                self.requires.add("OpenSSL/1.0.2h@lasote/stable")

    def build(self):
        cmake = CMake(self.settings)
        if "OpenSSL" in self.requires:
            lib_path = self.deps_cpp_info["OpenSSL"].lib_paths[0]
            openssl_root_dir = os.path.dirname(lib_path)
            self.run("cmake -DENABLE_SSL_SUPPORT=ON -DOPENSSL_ROOT_DIR=%s -DBUILD_EXAMPLES=OFF %s/rabbitmq-c %s" % (openssl_root_dir, self.conanfile_directory, cmake.command_line))
        else:
            self.run("cmake -DENABLE_SSL_SUPPORT=OFF -DBUILD_EXAMPLES=OFF %s/rabbitmq-c %s" % (self.conanfile_directory, cmake.command_line))

        self.run("cmake --build . %s" % cmake.build_config)
        self.run("make -C %s test" % self.conanfile_directory)

    def package(self):
        self.copy("amqp.h", dst="include", src="rabbitmq-c/librabbitmq")
        self.copy("amqp_tcp_socket.h", dst="include", src="rabbitmq-c/librabbitmq")
        self.copy("amqp_ssl_socket.h", dst="include", src="rabbitmq-c/librabbitmq")
        self.copy("amqp_framing.h", dst="include", src="rabbitmq-c/librabbitmq")
        self.copy("*.lib", dst="lib", src="librabbitmq")
        self.copy("*.a", dst="lib", src="librabbitmq")
        self.copy("*.so.*", dst="lib", src="librabbitmq")
        self.copy("*.dll", dst="lib", src="librabbitmq")

    def package_info(self):
        self.cpp_info.libs = ["rabbitmq"]
