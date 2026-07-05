class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int, int>>> adj(n + 1);

        for (auto& r : roads) {
            int a = r[0], b = r[1], d = r[2];
            adj[a].push_back({b, d});
            adj[b].push_back({a, d});
        }

        vector<int> vis(n + 1, 0);
        queue<int> q;
        q.push(1);
        vis[1] = 1;

        int ans = INT_MAX;

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            for (auto [nei, dist] : adj[node]) {
                ans = min(ans, dist);

                if (!vis[nei]) {
                    vis[nei] = 1;
                    q.push(nei);
                }
            }
        }

        return ans;
    }
};