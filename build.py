from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="filonovpv")
    builder.add_common_builds(pure_c=True)
    builder.run()
