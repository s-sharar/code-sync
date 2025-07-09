class Solution {
public:
    struct Stack{
        stack<int> s, sMax;
        bool empty() const {
            return s.empty();
        }
        void push(int i) {
            sMax.push(std::max(max(), i));
            s.push(i);
        }
        int pop() {
            sMax.pop();
            auto x = s.top();
            s.pop();
            return x;
        }

        int max() const {
            if (empty()) return INT_MIN;
            return sMax.top();
        }
    };
    
    Stack sStart, sEnd;

    void add(int i) {
        sEnd.push(i);
    }

    void remove() {
        if (sStart.empty()) {
            while (!sEnd.empty()) {
                sStart.push(sEnd.pop());
            }
        }
        sStart.pop();
    }

    int maxElem() {
        return max(sStart.max(), sEnd.max());
    }

    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        if (nums.size() < k) return {};
        for (int i = 0; i < k - 1; ++i) {
            add(nums[i]);
        }
        vector<int> res;
        for (int r = k - 1; r < nums.size(); ++r) {
            add(nums[r]);
            res.push_back(maxElem());
            remove();
        }
        return res;
    }
};