#include <bits/stdc++.h>
using namespace std;

class FrontMiddleBackQueue {
    deque<int> L, R;

    void rebalance() {
        // want |L| == |R| or |L| == |R| + 1
        if (L.size() < R.size()) {
            L.push_back(R.front());
            R.pop_front();
        } else if (L.size() > R.size() + 1) {
            R.push_front(L.back());
            L.pop_back();
        }
    }

public:
    FrontMiddleBackQueue() {}

    void pushFront(int val) {
        L.push_front(val);
        rebalance();
    }

    void pushMiddle(int val) {
        // if odd, L has the middle at its back; insert BEFORE it
        if (L.size() > R.size()) {
            R.push_front(L.back());
            L.pop_back();
        }
        L.push_back(val);
        // rebalance(); // not necessary, but harmless if you keep it
    }

    void pushBack(int val) {
        R.push_back(val);
        rebalance();
    }

    int popFront() {
        if (L.empty() && R.empty()) return -1;
        int ans = L.front();
        L.pop_front();
        rebalance();
        return ans;
    }

    int popMiddle() {
        if (L.empty() && R.empty()) return -1;
        int ans = L.back();   // frontmost middle always lives here
        L.pop_back();
        rebalance();
        return ans;
    }

    int popBack() {
        if (L.empty() && R.empty()) return -1;
        int ans;
        if (!R.empty()) {
            ans = R.back();
            R.pop_back();
        } else {
            ans = L.back();
            L.pop_back();
        }
        rebalance();
        return ans;
    }
};