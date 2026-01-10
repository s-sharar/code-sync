class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums, int x) {
        if (x == 0) return 0; // because i=j is allowed when |i-j|>=0

        set<int> seen;
        int ans = INT_MAX;

        for (int i = x; i < (int)nums.size(); ++i) {
            seen.insert(nums[i - x]);

            auto it = seen.lower_bound(nums[i]);   // first >= nums[i]
            if (it != seen.end())
                ans = min(ans, *it - nums[i]);
            if (it != seen.begin())
                ans = min(ans, nums[i] - *prev(it));
        }
        return ans;
    }
};