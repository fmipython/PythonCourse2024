#ifndef ARRAYS_POINTERS_H
#define ARRAYS_POINTERS_H

#include <stdio.h>
#include <stdlib.h>

struct DynamicArray{
    int* items;
    int capacity;
    int size;
};

extern struct DynamicArray create(const int capacity);
extern struct DynamicArray create_from_raw(const int* items, const int capacity);
extern void add(struct DynamicArray* instance, const int item);
extern int get(const struct DynamicArray* instance, const int index);
extern void resize(struct DynamicArray* instance);
extern void destruct(struct DynamicArray* instance);

#endif