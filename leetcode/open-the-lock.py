class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead(deadends.begin(), deadends.end());
        if (dead.count("0000")) return -1;
        if (target == "0000") return 0;

        queue<pair<string,int>> q;
        unordered_set<string> vis;
        q.push({"0000", 0});
        vis.insert("0000");

        auto neighbors = [&](const string& s) {
            vector<string> res;
            res.reserve(8);
            for (int i = 0; i < 4; ++i) {
                string up = s, down = s;
                up[i] = (s[i] == '9') ? '0' : (s[i] + 1);
                down[i] = (s[i] == '0') ? '9' : (s[i] - 1);
                res.push_back(up);
                res.push_back(down);
            }
            return res;
        };

        while (!q.empty()) {
            auto [cur, d] = q.front(); q.pop();
            for (auto& nxt : neighbors(cur)) {
                if (dead.count(nxt) || vis.count(nxt)) continue;
                if (nxt == target) return d + 1;
                vis.insert(nxt);
                q.push({nxt, d + 1});
            }
        }
        return -1;
    }
};