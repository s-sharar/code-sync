class Solution {
    long long atMost(const vector<int>& nums, int K) {
        if (K < 0) return 0;
        int l = 0, odd = 0;
        long long res = 0;
        for (int r = 0; r < (int)nums.size(); ++r) {
            odd += (nums[r] & 1);
            while (odd > K) {
                odd -= (nums[l] & 1);
                ++l;
            }
            res += (r - l + 1);
        }
        return res;
    }

public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        return (int)(atMost(nums, k) - atMost(nums, k - 1));
    }
};