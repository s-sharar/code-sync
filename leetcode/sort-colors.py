class Solution {
public:
    void sortColors(vector<int>& nums) {
        int cnt[3] = {0, 0, 0};
        for (int x : nums) cnt[x]++;

        int idx = 0;
        for (int v = 0; v < 3; v++) {
            for (int k = 0; k < cnt[v]; k++) {
                nums[idx++] = v;
            }
        }
    }
};