class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int ans = 0, a = 0, b = 0;
        for (int x : nums) ans ^= x;
        unsigned int diff = ans & -(unsigned int)ans;
        for (int x : nums) {
            if (x & diff) a ^= x;
            else b ^= x;
        }
        return {a, b};
    }
};