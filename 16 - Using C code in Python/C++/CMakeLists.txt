cmake_minimum_required(VERSION 3.16)
project(DynamicArray)

set(CMAKE_CXX_STANDARD 11)

add_library(DynamicArray SHARED dynamic_array.cpp dynamic_array.h)