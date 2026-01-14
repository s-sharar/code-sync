#include <queue>
#include <vector>
using namespace std;

class MedianFinder {
    // small: max-heap (lower half)
    priority_queue<int> small;

    // large: min-heap (upper half)
    priority_queue<int, vector<int>, greater<int>> large;

public:
    MedianFinder() {}

    void addNum(int num) {
        // 1) put into lower half first
        small.push(num);

        // 2) enforce order: everything in small <= everything in large
        large.push(small.top());
        small.pop();

        // 3) enforce size: small is allowed to have at most 1 extra element
        if (large.size() > small.size()) {
            small.push(large.top());
            large.pop();
        }
    }

    double findMedian() {
        if (small.size() == large.size()) {
            // avoid overflow
            return ((double)small.top() + (double)large.top()) / 2.0;
        }
        // small has one extra
        return (double)small.top();
    }
};