class Solution {
    unordered_map<string, vector<string>> adj;
    vector<string> res;
    unordered_map<string, int> it;
    void dfs(const string &node) {
        while (it[node] < adj[node].size()) {
            int idx = it[node];
            string nei = adj[node][idx];
            ++it[node];
            dfs(nei);
        }
        res.push_back(node);
    }
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for (auto &ticket : tickets) {
            adj[ticket[0]].push_back(ticket[1]);
            it[ticket[0]] = 0;
        }
        for (auto &elem : adj) {
            sort(elem.second.begin(), elem.second.end());
        }
        dfs("JFK");
        reverse(res.begin(), res.end());
        return res;
    }
};