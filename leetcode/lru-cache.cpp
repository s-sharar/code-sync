#include <unordered_map>
using namespace std;

class LRUCache {
    struct Node {
        int key, val;
        Node *prev, *next;
        Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
    };

    int cap;
    unordered_map<int, Node*> mp;
    Node *head, *tail; // sentinels: head <-> ... <-> tail

    void remove(Node* x) { // unlink x from list
        x->prev->next = x->next;
        x->next->prev = x->prev;
    }

    void pushFront(Node* x) { // insert right after head
        x->next = head->next;
        x->prev = head;
        head->next->prev = x;
        head->next = x;
    }

    void touch(Node* x) { // mark as most-recently used
        remove(x);
        pushFront(x);
    }

public:
    LRUCache(int capacity) : cap(capacity) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        auto it = mp.find(key);
        if (it == mp.end()) return -1;
        Node* x = it->second;
        touch(x);
        return x->val;
    }

    void put(int key, int value) {
        auto it = mp.find(key);
        if (it != mp.end()) {
            Node* x = it->second;
            x->val = value;
            touch(x);
            return;
        }

        Node* x = new Node(key, value);
        mp[key] = x;
        pushFront(x);

        if ((int)mp.size() > cap) {
            Node* lru = tail->prev;   // last real node
            remove(lru);
            mp.erase(lru->key);
            delete lru;
        }
    }

    ~LRUCache() {
        Node* cur = head;
        while (cur) {
            Node* nxt = cur->next;
            delete cur;
            cur = nxt;
        }
    }
};