class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int maxOr = 0;
        for (int x : nums) maxOr |= x;

        int n = nums.size();
        int ans = 0;

        function<void(int,int)> dfs = [&](int i, int curOr) {
            if (i == n) {
                if (curOr == maxOr) ans++;
                return;
            }
            // skip
            dfs(i + 1, curOr);
            // take
            dfs(i + 1, curOr | nums[i]);
        };

        dfs(0, 0);
        return ans;
    }
};