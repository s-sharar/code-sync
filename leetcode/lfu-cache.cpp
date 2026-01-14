#include <bits/stdc++.h>
using namespace std;

class LFUCache {
    struct Node {
        int val;
        int freq;
        list<int>::iterator it; // points to position in buckets[freq]
    };

    int cap;
    int minFreq;
    unordered_map<int, Node> mp;              // key -> Node
    unordered_map<int, list<int>> buckets;    // freq -> keys (front=MRU, back=LRU)

    void touch(int key) {
        auto &node = mp[key];
        int f = node.freq;

        // remove from old freq list
        buckets[f].erase(node.it);
        if (buckets[f].empty()) {
            buckets.erase(f);
            if (minFreq == f) minFreq++;
        }

        // add to new freq list
        node.freq++;
        buckets[node.freq].push_front(key);
        node.it = buckets[node.freq].begin();
    }

public:
    LFUCache(int capacity) : cap(capacity), minFreq(0) {}

    int get(int key) {
        if (!mp.count(key)) return -1;
        touch(key);
        return mp[key].val;
    }

    void put(int key, int value) {
        if (cap == 0) return;

        if (mp.count(key)) {
            mp[key].val = value;
            touch(key);
            return;
        }

        // evict if full
        if ((int)mp.size() == cap) {
            int evictKey = buckets[minFreq].back();  // LRU among minFreq
            buckets[minFreq].pop_back();
            if (buckets[minFreq].empty()) buckets.erase(minFreq);
            mp.erase(evictKey);
        }

        // insert new
        minFreq = 1;
        buckets[1].push_front(key);
        mp[key] = Node{value, 1, buckets[1].begin()};
    }
};