class Solution {
    vector<vector<int>> graph;
    vector<int> disc;
    vector<int> low;
    vector<vector<int>> bridges;
    int timer = 0;

    void dfs(int u, int parent) {
        disc[u] = low[u] = timer++;

        for (int v : graph[u]) {
            if (v == parent) continue;

            if (disc[v] == -1) {
                // Tree edge
                dfs(v, u);

                // v's subtree may have found a route upward
                low[u] = min(low[u], low[v]);

                // No alternate route from v's subtree to u or above
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v});
                }
            } else {
                // Back edge to an already visited node
                low[u] = min(low[u], disc[v]);
            }
        }
    }

public:
    vector<vector<int>> criticalConnections(
        int n,
        vector<vector<int>>& connections
    ) {
        graph.resize(n);

        for (auto& edge : connections) {
            int u = edge[0];
            int v = edge[1];

            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        disc.assign(n, -1);
        low.assign(n, -1);

        dfs(0, -1);

        return bridges;
    }
};