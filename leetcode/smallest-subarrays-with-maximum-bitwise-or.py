class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> ans(n, 1);
        vector<int> last(32, -1); // last position where bit b is set

        for (int i = n - 1; i >= 0; --i) {
            for (int b = 0; b < 32; ++b) {
                if ((nums[i] >> b) & 1) last[b] = i;
            }
            int far = i;
            for (int b = 0; b < 32; ++b) {
                if (last[b] != -1) far = max(far, last[b]);
            }
            ans[i] = far - i + 1;
        }
        return ans;
    }
};