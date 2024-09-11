class DynamicArray {
    public:
        DynamicArray(const int capacity);
        DynamicArray(const int* items, const int capacity);

        void add(const int item);
        int get(const int index) const;
        void resize();

        ~DynamicArray();
    private:
        int* items;
        int capacity;
        int size;
};

extern "C" {
    DynamicArray* create(const int capacity) {
        return new DynamicArray(capacity);
    }
    DynamicArray* create_from_raw(const int* items, const int capacity) {
        return new DynamicArray(items, capacity);
    }
    void add(DynamicArray* instance, const int item) {
        instance->add(item);
    }
    int get(const DynamicArray* instance, const int index) {
        return instance->get(index);
    }
    void resize(DynamicArray* instance) {
        instance->resize();
    }
    void destruct(DynamicArray* instance) {
        delete instance;
    }
}