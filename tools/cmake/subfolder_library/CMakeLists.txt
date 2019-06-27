cmake_minimum_required(VERSION 2.6)
project(Modules)

include_directories ("${PROJECT_SOURCE_DIR}/include")

add_subdirectory ("${PROJECT_SOURCE_DIR}/lib/laugh")
set (EXTRA_LIBS ${EXTRA_LIBS} Laugh)

# add the executable
add_executable (main main.cc)
target_link_libraries (main ${EXTRA_LIBS})