class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails;
        tails.reserve(nums.size());

        for (int x : nums) {
            auto it = lower_bound(tails.begin(), tails.end(), x); // first >= x
            if (it == tails.end()) tails.push_back(x);
            else *it = x;
        }
        return (int)tails.size();
    }
};