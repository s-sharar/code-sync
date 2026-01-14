class MyCircularQueue {
    vector<int> a;
    int head;   // index of front element
    int sz;     // current size
    int cap;    // capacity

public:
    MyCircularQueue(int k) : a(k), head(0), sz(0), cap(k) {}

    bool enQueue(int value) {
        if (isFull()) return false;
        int tail = (head + sz) % cap;   // next free slot
        a[tail] = value;
        sz++;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % cap;
        sz--;
        return true;
    }

    int Front() {
        if (isEmpty()) return -1;
        return a[head];
    }

    int Rear() {
        if (isEmpty()) return -1;
        int tailIdx = (head + sz - 1) % cap;
        return a[tailIdx];
    }

    bool isEmpty() { return sz == 0; }
    bool isFull()  { return sz == cap; }
};