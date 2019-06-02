cmake_minimum_required(VERSION 3.0)
project(use_config 
  VERSION 1.0
  )

cmake_host_system_information(RESULT OS_NAME QUERY OS_NAME)
set(AUTHOR hxzhao)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/config.h.in"
  "${PROJECT_BINARY_DIR}/config.h"
  )

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")
 
# add the executable
add_executable(main main.cc)