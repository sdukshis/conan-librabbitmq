cmake_minimum_required(VERSION 2.8.12)
project(TestLibrabbitmq)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test_librabbitmq test_rabbitmq.cpp)
target_link_libraries(test_librabbitmq ${CONAN_LIBS})
