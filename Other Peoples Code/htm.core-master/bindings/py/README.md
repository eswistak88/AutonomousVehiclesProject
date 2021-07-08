
## Layout of directories:
```
  REPO_DIR
    bindings
        py   -- Location of Python bindings
          packaging -- Contains things needed to build package
          cpp_src 
            bindings  -- C++ pybind11 mapping source code 
            plugin    -- C++ code to manage python plugin
        tests       -- Unit test for python interface
```

## This is where we build the distribution package:
```
  REPO_DIR
     build
        Release
            bin         --- Contains executables for unit tests and examples
            include     --- Include C++ header files
            lib         --- Static & Dynamic compiled libraries for htm core found here
          - distr                            ( copy from REPO_DIR/bindings/py/packaging/* by CMake)
         /      build                   -- setup.py; setup() puts stuff in here