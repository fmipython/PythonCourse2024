cmake_minimum_required(VERSION 3.15)
project(SimpleFunction C)

set(CMAKE_C_STANDARD 99)

add_library(SimpleFunction SHARED sum.c sum.h)