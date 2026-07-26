class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indeg(numCourses, 0);
        vector<int> res;
        for (const auto &pre : prerequisites) {
            adj[pre[1]].push_back(pre[0]);
            indeg[pre[0]]++;
        }
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (!indeg[i]) q.push(i);
        }
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            res.push_back(node);
            for (auto nei : adj[node]) {
                if (--indeg[nei] == 0) q.push(nei);
            }
        }

        if (res.size() != numCourses) return {};
        return res;
    }
};