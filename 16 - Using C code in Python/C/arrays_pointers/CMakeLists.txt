cmake_minimum_required(VERSION 3.16)
project(SimpleFunction C)

set(CMAKE_C_STANDARD 99)

add_library(DynamicArray SHARED dynamic_array.c dynamic_array.h)