class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0};

        vector<vector<int>> g(n);
        vector<int> deg(n, 0);

        for (auto &e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
            deg[u]++; deg[v]++;
        }

        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (deg[i] == 1) q.push(i);
        }

        int remaining = n;
        while (remaining > 2) {
            int sz = q.size();
            remaining -= sz;
            while (sz--) {
                int leaf = q.front(); q.pop();
                for (int nei : g[leaf]) {
                    if (--deg[nei] == 1) q.push(nei);
                }
            }
        }

        vector<int> ans;
        while (!q.empty()) { ans.push_back(q.front()); q.pop(); }
        return ans;
    }
};