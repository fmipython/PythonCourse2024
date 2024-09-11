#include "dynamic_array.h"

struct DynamicArray create(const int capacity) {
    struct DynamicArray instance;

    instance.capacity = capacity;
    instance.size = 0;
    instance.items = malloc(sizeof(int) * capacity);
    
    return instance;
}

struct DynamicArray create_from_raw(const int* items, const int capacity) {
    struct DynamicArray instance;

    instance.capacity = capacity;
    instance.size = capacity;
    instance.items = malloc(sizeof(int) * capacity);

    for (int i = 0; i < capacity; i++) {
        instance.items[i] = items[i];
    }

    return instance;
}

void add(struct DynamicArray* instance, const int item) {
    if (instance->capacity == instance->size) {
        resize(instance);
    }

    instance->items[instance->size++] = item;
}

int get(const struct DynamicArray* instance, const int index) {
    if (index >= instance->size || index < 0) {
        printf("Index %d out of bounds for size %d", index, instance->size);
    }

    return instance->items[index];
}

void resize(struct DynamicArray* instance) {
    instance->capacity *= 2;
    instance->items = realloc(instance->items, sizeof(int) * instance->capacity);
}

void destruct(struct DynamicArray* instance) {
    free(instance->items);
}
