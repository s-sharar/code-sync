class Solution {
    void dfs(vector<int>& nums, vector<int>& path, vector<int>& used,
             vector<vector<int>>& res) {
        if ((int)path.size() == (int)nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (used[i]) continue;
            used[i] = 1;
            path.push_back(nums[i]);
            dfs(nums, path, used, res);
            path.pop_back();
            used[i] = 0;
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        vector<int> used(nums.size(), 0);
        dfs(nums, path, used, res);
        return res;
    }
};