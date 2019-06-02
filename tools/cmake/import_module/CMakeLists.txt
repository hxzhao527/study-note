cmake_minimum_required(VERSION 2.6)
project(Modules)

# should we use our own math functions?
option (USE_MYMATH 
        "Use project provided math implementation" ON)

# add the FakeLib library?
# notice: condition is `USE_MYMATH MATCHES ON` not `USE_MYMATH`
if (USE_MYMATH MATCHES ON)
  include_directories ("${PROJECT_SOURCE_DIR}/fakelib")
  add_subdirectory (fakelib)
  set (EXTRA_LIBS ${EXTRA_LIBS} FakeLib)
  add_compile_definitions(USE_MYMATH)
endif ()

# add the executable
add_executable (main main.cc)
target_link_libraries (main ${EXTRA_LIBS})