class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = (int)graph.size();
        vector<vector<int>> ans;
        vector<int> path;
        path.push_back(0);

        function<void(int)> dfs = [&](int u) {
            if (u == n - 1) {
                ans.push_back(path);
                return;
            }
            for (int v : graph[u]) {
                path.push_back(v);
                dfs(v);
                path.pop_back();
            }
        };

        dfs(0);
        return ans;
    }
};