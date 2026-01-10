class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        unordered_map<int, long long> freq;
        long long res = 0;
        long long pairs = 0;  // number of equal pairs in current window
        int l = 0;

        for (int r = 0; r < (int)nums.size(); ++r) {
            long long f = freq[nums[r]];
            pairs += f;        // adding nums[r] creates f new pairs with existing same values
            freq[nums[r]] = f + 1;

            while (pairs >= k) {
                long long fl = freq[nums[l]];
                pairs -= (fl - 1); // removing nums[l] destroys (fl-1) pairs
                freq[nums[l]] = fl - 1;
                ++l;
            }

            // after shrinking, pairs < k.
            // all subarrays ending at r that start before l are good
            res += l;
        }
        return res;
    }
};