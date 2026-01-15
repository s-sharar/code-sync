class Solution {
public:
    int maxNonDecreasingLength(vector<int>& nums1, vector<int>& nums2) {
        int n = (int)nums1.size();
        int dpA = 1, dpB = 1;   // ending at i-1
        int ans = 1;

        for (int i = 1; i < n; ++i) {
            int newA = 1, newB = 1;

            if (nums1[i] >= nums1[i-1]) newA = max(newA, dpA + 1);
            if (nums1[i] >= nums2[i-1]) newA = max(newA, dpB + 1);

            if (nums2[i] >= nums1[i-1]) newB = max(newB, dpA + 1);
            if (nums2[i] >= nums2[i-1]) newB = max(newB, dpB + 1);

            dpA = newA;
            dpB = newB;
            ans = max(ans, max(dpA, dpB));
        }
        return ans;
    }
};