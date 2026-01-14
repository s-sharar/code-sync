class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long long s1 = 0, s2 = 0;
        long long z1 = 0, z2 = 0;

        for (int x : nums1) {
            if (x == 0) z1++;
            else s1 += x;
        }
        for (int x : nums2) {
            if (x == 0) z2++;
            else s2 += x;
        }

        long long base1 = s1 + z1;
        long long base2 = s2 + z2;

        if (base1 == base2) return base1;

        if (base1 < base2) {
            return (z1 == 0) ? -1 : base2;
        } else {
            return (z2 == 0) ? -1 : base1;
        }
    }
};