class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();
        int l = 0;
        int res = -1;
        unordered_map<int, int> cnt;
        for (int r = 0; r < n; ++r) {
            cnt[fruits[r]]++;
            while (cnt.size() > 2) {
                cnt[fruits[l]]--;
                if (cnt[fruits[l]] == 0) cnt.erase(fruits[l]);
                ++l;
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};