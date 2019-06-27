cmake_minimum_required(VERSION 3.0)

project(Third)

# include("${PROJECT_SOURCE_DIR}/cmake/FindFFMPEG.cmake")
list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")

# search zlib
find_package(ZLIB REQUIRED)
find_package(FFMPEG REQUIRED)

# if found, include and link
if(ZLIB_FOUND)
    include_directories( ${ZLIB_INCLUDE_DIRS} )
    set (EXTRA_LIBS ${EXTRA_LIBS} ${ZLIB_LIBRARIES})    
endif(ZLIB_FOUND)

add_executable(main main.cc)
target_link_libraries(main ${EXTRA_LIBS})