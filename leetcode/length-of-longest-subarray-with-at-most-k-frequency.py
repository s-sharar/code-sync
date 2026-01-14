class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        int l = 0;
        int res = INT_MIN;
        for (int r = 0; r < nums.size(); ++r) {
            cnt[nums[r]]++;
            while (cnt[nums[r]] > k) {
                --cnt[nums[l]];
                ++l;
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};