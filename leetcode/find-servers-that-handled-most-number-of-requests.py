class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        int n = (int)arrival.size();
        vector<int> cnt(k, 0);

        // (endTime, serverId)
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> busy;

        set<int> free;
        for (int i = 0; i < k; ++i) free.insert(i);

        for (int i = 0; i < n; ++i) {
            long long t = arrival[i];

            // release finished servers
            while (!busy.empty() && busy.top().first <= t) {
                free.insert(busy.top().second);
                busy.pop();
            }

            if (free.empty()) continue; // drop

            int start = i % k;
            auto it = free.lower_bound(start);
            if (it == free.end()) it = free.begin(); // wrap

            int id = *it;
            free.erase(it);

            cnt[id]++;
            busy.push({t + load[i], id});
        }

        int mx = 0;
        for (int c : cnt) mx = max(mx, c);

        vector<int> res;
        for (int i = 0; i < k; ++i) {
            if (cnt[i] == mx) res.push_back(i);
        }
        return res;
    }
};