cmake_minimum_required(VERSION 3.15)
project(Structs C)

set(CMAKE_C_STANDARD 99)

add_library(Structs SHARED rational.c rational.h)