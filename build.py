from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(mingw_configurations=[],
                                 archs=["x86_64"])
    builder.add_common_builds(pure_c=True)
    builder.run()
