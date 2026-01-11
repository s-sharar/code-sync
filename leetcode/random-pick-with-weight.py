class Solution {
    vector<int> pref;
    int total;
    std::mt19937 rng;

public:
    Solution(vector<int>& w) : total(0), rng(std::random_device{}()) {
        pref.reserve(w.size());
        for (int x : w) {
            total += x;
            pref.push_back(total);
        }
    }

    int pickIndex() {
        std::uniform_int_distribution<int> dist(1, total);
        int r = dist(rng);
        int idx = (int)(lower_bound(pref.begin(), pref.end(), r) - pref.begin());
        return idx;
    }
};