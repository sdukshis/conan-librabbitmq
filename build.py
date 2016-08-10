from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    mingw_configurations = [("4.9", "x86_64", "seh", "posix"),
                            ("4.9", "x86_64", "sjlj", "posix"),
                            ("4.9", "x86", "sjlj", "posix"),
                            ("4.9", "x86", "dwarf2", "posix")]
    builder = ConanMultiPackager(mingw_configurations=mingw_configurations,
                                 archs=["x86_64"])
    builder.add_common_builds(pure_c=True)
    builder.run()
