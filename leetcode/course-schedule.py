class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses);
        for (auto elem : prerequisites) {
            adj[elem[0]].push_back(elem[1]);
            indegree[elem[1]]++;
        }
        queue<int> q;
        int res = 0;
        for (int i = 0; i < numCourses; ++i) {
            if (!indegree[i]) {
                q.push(i);
                ++res;
            }
        }
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (auto nei : adj[node]) {
                if (--indegree[nei] == 0) {
                    q.push(nei);
                    ++res;
                }
            }
        }
        return res == numCourses;

    }
};