class DSU {
    vector<int> parent, rankv;
public:
    DSU(int n): parent(n), rankv(n,0) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }
    void unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return;
        if (rankv[a] < rankv[b]) swap(a,b);
        parent[b] = a;
        if (rankv[a] == rankv[b]) rankv[a]++;
    }
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, int> emailId;
        unordered_map<string, string> emailName; // email -> name
        int id = 0;

        // 1) assign ids to emails
        for (auto &acc : accounts) {
            string name = acc[0];
            for (int i = 1; i < (int)acc.size(); ++i) {
                string &email = acc[i];
                if (!emailId.count(email)) {
                    emailId[email] = id++;
                    emailName[email] = name;
                }
            }
        }

        DSU dsu(id);

        // 2) union emails within each account
        for (auto &acc : accounts) {
            int first = emailId[acc[1]];
            for (int i = 2; i < (int)acc.size(); ++i) {
                dsu.unite(first, emailId[acc[i]]);
            }
        }

        // 3) group emails by root
        unordered_map<int, vector<string>> groups;
        groups.reserve(id);
        for (auto &kv : emailId) {
            const string &email = kv.first;
            int eid = kv.second;
            int root = dsu.find(eid);
            groups[root].push_back(email);
        }

        // 4) build result
        vector<vector<string>> res;
        res.reserve(groups.size());
        for (auto &kv : groups) {
            auto &emails = kv.second;
            sort(emails.begin(), emails.end());
            string name = emailName[emails[0]];
            vector<string> merged;
            merged.reserve(emails.size() + 1);
            merged.push_back(name);
            merged.insert(merged.end(), emails.begin(), emails.end());
            res.push_back(move(merged));
        }
        return res;
    }
};