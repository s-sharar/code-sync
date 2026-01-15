class Solution {
    void dfs(int i, int target, vector<int>& cand, vector<int>& cur,
             vector<vector<int>>& res) {
        if (target == 0) {
            res.push_back(cur);
            return;
        }
        if (target < 0 || i == (int)cand.size()) return;

        // take cand[i] (stay at i because we can reuse it)
        cur.push_back(cand[i]);
        dfs(i, target - cand[i], cand, cur, res);
        cur.pop_back();

        // skip cand[i] (move to next index)
        dfs(i + 1, target, cand, cur, res);
    }

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end()); // optional pruning
        vector<vector<int>> res;
        vector<int> cur;
        dfs(0, target, candidates, cur, res);
        return res;
    }
};