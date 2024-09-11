#include "dynamic_array.h"

DynamicArray::DynamicArray(const int capacity): capacity(capacity), size(0) {
    this->items = new int[this->capacity];
}
DynamicArray::DynamicArray(const int* items, const int capacity): capacity(capacity) {
    this->items = new int[this->capacity];
    for (int i = 0; i < this->capacity; i++) {
        this->items[i] = items[i];
    }
    this->size = this->capacity;
}

void DynamicArray::add(const int item) {
    if (this->size == this->capacity) {
        this->resize();
    }
    this->items[this->size] = item;
    this->size++;
}
int DynamicArray::get(const int index) const {
    if (index < 0 || index >= this->size) {
        throw "Index out of bounds";
    }
    return this->items[index];
}
void DynamicArray::resize() {
    int* new_items = new int[this->capacity * 2];
    for (int i = 0; i < this->capacity; i++) {
        new_items[i] = this->items[i];
    }
    delete[] this->items;
    this->items = new_items;
    this->capacity *= 2;
}

DynamicArray::~DynamicArray() {
    delete[] this->items;
}