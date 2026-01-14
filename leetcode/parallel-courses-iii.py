class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<vector<int>> adj(n);
        vector<int> indegree(n, 0);

        for (auto &r : relations) {
            int u = r[0] - 1, v = r[1] - 1;
            adj[u].push_back(v);
            indegree[v]++;
        }

        queue<int> q;
        vector<int> dp(n, 0); // earliest finish time

        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
                dp[i] = time[i]; // can start immediately
            }
        }

        while (!q.empty()) {
            int u = q.front(); q.pop();

            for (int v : adj[u]) {
                // u must finish before v can start
                dp[v] = max(dp[v], dp[u] + time[v]);

                if (--indegree[v] == 0) {
                    q.push(v);
                }
            }
        }

        return *max_element(dp.begin(), dp.end());
    }
};