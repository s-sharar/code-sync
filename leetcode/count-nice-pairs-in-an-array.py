class Solution {
public:
    static constexpr int MOD = 1'000'000'007;

    int rev(int x) {
        int r = 0;
        while (x > 0) {
            r = r * 10 + (x % 10);
            x /= 10;
        }
        return r;
    }

    int countNicePairs(vector<int>& nums) {
        unordered_map<int, long long> freq;
        long long ans = 0;

        for (int x : nums) {
            int key = x - rev(x);
            ans = (ans + freq[key]) % MOD;
            freq[key]++;
        }
        return (int)ans;
    }
};