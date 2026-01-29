class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> cnt;
        cnt[0] = 1;                 // empty prefix
        int pref = 0;
        int ans = 0;

        for (int x : nums) {
            pref += x;
            auto it = cnt.find(pref - k);
            if (it != cnt.end()) ans += it->second;
            cnt[pref]++;
        }
        return ans;
    }
};