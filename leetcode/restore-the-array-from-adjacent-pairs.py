class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, vector<int>> adj;
        adj.reserve(adjacentPairs.size() * 2);

        for (const auto& p : adjacentPairs) {
            adj[p[0]].push_back(p[1]);
            adj[p[1]].push_back(p[0]);
        }

        int start = 0;
        for (const auto& [x, nbrs] : adj) {
            if ((int)nbrs.size() == 1) { start = x; break; }
        }

        int n = (int)adjacentPairs.size() + 1;
        vector<int> res(n);
        res[0] = start;
        res[1] = adj[start][0];

        for (int i = 2; i < n; ++i) {
            auto& nbrs = adj[res[i - 1]];
            // pick the neighbor that's not the previous element
            res[i] = (nbrs[0] == res[i - 2]) ? nbrs[1] : nbrs[0];
        }

        return res;
    }
};