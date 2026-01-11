class Solution {
    int atMost(vector<int> &nums, int k) {
        unordered_map<int, int> count;
        int l = 0;
        int res = 0;
        int diff = 0;
        for (int r = 0; r < nums.size(); ++r) {
            count[nums[r]]++;
            if (count[nums[r]] == 1) ++diff;
            while (diff > k) {
                count[nums[l]]--;
                if (count[nums[l]] == 0) --diff;
                ++l;
            }
            res += r - l + 1;
        }
        return res;
    }
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }
};