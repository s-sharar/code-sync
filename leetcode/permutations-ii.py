class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        vector<int> cur;
        vector<int> used(nums.size(), 0);

        function<void()> dfs = [&]() {
            if (cur.size() == nums.size()) {
                ans.push_back(cur);
                return;
            }
            for (int i = 0; i < (int)nums.size(); ++i) {
                if (used[i]) continue;
                if (i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue; // key line

                used[i] = 1;
                cur.push_back(nums[i]);
                dfs();
                cur.pop_back();
                used[i] = 0;
            }
        };

        dfs();
        return ans;
    }
};