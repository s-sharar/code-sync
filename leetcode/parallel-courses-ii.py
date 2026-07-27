class Solution {
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& relations, int k) {
        vector<int> pre(n, 0);

        for (auto& edge : relations) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            pre[v] |= 1 << u;
        }

        int total = 1 << n;
        vector<int> dp(total, INT_MAX);
        dp[0] = 0;

        for (int mask = 0; mask < total; mask++) {
            if (dp[mask] == INT_MAX) continue;

            int available = 0;

            for (int i = 0; i < n; i++) {
                if (!(mask & (1 << i)) &&
                    (mask & pre[i]) == pre[i]) {
                    available |= 1 << i;
                }
            }

            if (__builtin_popcount(available) <= k) {
                int nextMask = mask | available;
                dp[nextMask] = min(dp[nextMask], dp[mask] + 1);
            } else {
                for (int sub = available; sub; sub = (sub - 1) & available) {
                    if (__builtin_popcount(sub) == k) {
                        int nextMask = mask | sub;
                        dp[nextMask] = min(dp[nextMask], dp[mask] + 1);
                    }
                }
            }
        }

        return dp[total - 1];
    }
};