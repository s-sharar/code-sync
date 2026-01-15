class Solution {
    vector<int> topo(int V, vector<vector<int>>& adj, vector<int> indeg) {
        queue<int> q;
        for (int i = 0; i < V; i++) if (indeg[i] == 0) q.push(i);
        vector<int> order;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (--indeg[v] == 0) q.push(v);
            }
        }
        if ((int)order.size() != V) return {};
        return order;
    }

public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        // 1) assign unique groups for -1
        int G = m;
        for (int i = 0; i < n; i++) if (group[i] == -1) group[i] = G++;

        // items per group
        vector<vector<int>> itemsInGroup(G);
        for (int i = 0; i < n; i++) itemsInGroup[group[i]].push_back(i);

        // 2) build group graph + in-group item graph
        vector<vector<int>> groupAdj(G);
        vector<int> groupIndeg(G, 0);

        vector<vector<int>> inAdj(n);        // only in-group edges
        vector<int> inIndeg(n, 0);           // indegree counting only in-group prereqs

        // avoid duplicate group edges
        unordered_set<long long> seen;
        auto key = [&](int a, int b) -> long long { return (1LL * a << 32) ^ (unsigned)b; };

        for (int v = 0; v < n; v++) {
            for (int u : beforeItems[v]) { // u -> v
                int gu = group[u], gv = group[v];
                if (gu == gv) {
                    inAdj[u].push_back(v);
                    inIndeg[v]++;
                } else {
                    long long k = key(gu, gv);
                    if (!seen.count(k)) {
                        seen.insert(k);
                        groupAdj[gu].push_back(gv);
                        groupIndeg[gv]++;
                    }
                }
            }
        }

        // 3) topo sort groups
        vector<int> groupOrder = topo(G, groupAdj, groupIndeg);
        if (groupOrder.empty()) return {};

        // 4) topo sort items within each group
        vector<int> result;
        result.reserve(n);

        // We need a topo restricted to nodes in that group.
        // Do Kahn using only nodes of that group and their inAdj edges (which are already in-group only).
        for (int g : groupOrder) {
            auto& nodes = itemsInGroup[g];
            if (nodes.empty()) continue;

            queue<int> q;
            int cnt = 0;

            // local indeg copy for nodes in this group
            // (could avoid map by copying global inIndeg then restoring, but simplest is a local array)
            unordered_map<int,int> deg;
            deg.reserve(nodes.size() * 2);
            for (int x : nodes) deg[x] = inIndeg[x];

            for (int x : nodes) if (deg[x] == 0) q.push(x);

            while (!q.empty()) {
                int u = q.front(); q.pop();
                result.push_back(u);
                cnt++;
                for (int v : inAdj[u]) {
                    auto it = deg.find(v);
                    if (it == deg.end()) continue; // v not in this group (shouldn't happen since inAdj is in-group)
                    if (--(it->second) == 0) q.push(v);
                }
            }
            if (cnt != (int)nodes.size()) return {}; // cycle within group
        }

        return result;
    }
};