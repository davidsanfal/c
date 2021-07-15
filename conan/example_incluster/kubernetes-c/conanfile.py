from conans import ConanFile, CMake, tools


class KubernetesConan(ConanFile):
    name = "kubernetes"
    version = "0.0.1"
    topics = ("k8s", "kubernetes")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    requires = "libyaml/0.2.5", "openssl/1.1.1k", "libcurl/7.64.1"
    generators = "cmake", "cmake_find_package"

    def config_options(self):
        if self.settings.os == "Windows":
            raise ConanInvalidConfiguration("This library is not compatible with Windows")
        elif self.settings.os == "Macos":
            raise ConanInvalidConfiguration("This library is not compatible with Macos")

    def source(self):
        self.run("git clone https://github.com/kubernetes-client/c.git")
        tools.replace_in_file(
            "c/kubernetes/CMakeLists.txt",
            "find_package(OpenSSL)",
            "include(../../conanbuildinfo.cmake)\nconan_basic_setup()")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="c/kubernetes", build_folder="c/kubernetes/build")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/include", src="c/kubernetes/include")
        self.copy("*.h", dst="include/api", src="c/kubernetes/api")
        self.copy("*.h", dst="include/config", src="c/kubernetes/config")
        self.copy("*.h", dst="include/model", src="c/kubernetes/model")
        self.copy("*.h", dst="include/external", src="c/kubernetes/external")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["kubernetes"]
