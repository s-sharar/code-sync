class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        cnt[0] = 1;                 // empty prefix
        long long pref = 0;
        int res = 0;

        for (int x : nums) {
            pref += x;
            int r = (int)(pref % k);
            if (r < 0) r += k;      // normalize to [0, k-1]

            res += cnt[r];          // all previous same remainder
            cnt[r]++;
        }
        return res;
    }
};