class FenwickMax {
    vector<int> bit;
public:
    FenwickMax(int n) : bit(n + 1, 0) {}
    void update(int i, int val) {          // i is 0..N, internally use i+1
        for (i++; i < (int)bit.size(); i += i & -i)
            bit[i] = max(bit[i], val);
    }
    int query(int i) const {               // max on [0..i]
        int res = 0;
        for (i++; i > 0; i -= i & -i)
            res = max(res, bit[i]);
        return res;
    }
};

class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        int q = (int)queries.size();
        int N = min(50000, 3 * q); // constraints bound x by min(5e4, 3*q) :contentReference[oaicite:5]{index=5}

        // 1) Build final set of obstacles (all type-1 insertions)
        set<int> obs{0, N}; // sentinel bounds :contentReference[oaicite:6]{index=6}
        for (auto &qu : queries)
            if (qu[0] == 1) obs.insert(qu[1]);

        // 2) Initialize Fenwick with current gaps (gap is stored at RIGHT endpoint)
        FenwickMax fw(N + 1);
        for (auto it = obs.begin(); next(it) != obs.end(); ++it) {
            int a = *it, b = *next(it);
            fw.update(b, b - a);
        }

        // 3) Process in reverse
        vector<bool> ans;
        ans.reserve(q);

        for (int i = q - 1; i >= 0; --i) {
            auto &qu = queries[i];
            if (qu[0] == 1) {
                int x = qu[1];
                auto it = obs.find(x);
                int prv = *prev(it);
                int nxt = *next(it);
                obs.erase(it);

                // removing x merges (prv,x) and (x,nxt) into (prv,nxt)
                fw.update(nxt, nxt - prv); // only increases, so max-update is safe :contentReference[oaicite:7]{index=7}
            } else {
                int x = qu[1], sz = qu[2];
                auto it = obs.upper_bound(x);
                int prv = *prev(it); // last obstacle <= x :contentReference[oaicite:8]{index=8}

                bool ok = (fw.query(prv) >= sz) || (x - prv >= sz); // :contentReference[oaicite:9]{index=9}
                ans.push_back(ok);
            }
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};