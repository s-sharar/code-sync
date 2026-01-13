#include <vector>
#include <stack>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
    struct Stack {
        stack<int> s, sMax;

        void push(int a) {
            s.push(a);
            int prevMax = sMax.empty() ? INT_MIN : sMax.top();
            sMax.push(max(a, prevMax));
        }

        void pop() {
            s.pop();
            sMax.pop();
        }

        bool empty() const {
            return s.empty();
        }

        int maxElem() const {
            return sMax.empty() ? INT_MIN : sMax.top();
        }

        int top() const {
            return s.top();
        }
    };

    Stack sStart, sEnd;

    void add(int a) {
        sEnd.push(a);
    }

    void remove() {
        if (sStart.empty()) {
            while (!sEnd.empty()) {
                sStart.push(sEnd.top());
                sEnd.pop();
            }
        }
        sStart.pop();
    }

    int maxElemBoth() {
        return max(sStart.maxElem(), sEnd.maxElem());
    }

public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        if (k <= 0) return res;

        for (int i = 0; i < k - 1; ++i) add(nums[i]);

        for (int i = k - 1; i < (int)nums.size(); ++i) {
            add(nums[i]);
            res.push_back(maxElemBoth());
            remove();
        }
        return res;
    }
};