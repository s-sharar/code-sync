class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        int n = (int)events.size();
        sort(events.begin(), events.end(), [](const auto& a, const auto& b) {
            if (a[1] != b[1]) return a[1] < b[1]; // end
            return a[0] < b[0];                   // start
        });

        vector<int> ends(n);
        for (int i = 0; i < n; i++) ends[i] = events[i][1];

        // prev[i] = last index j < i with events[j].end < events[i].start
        vector<int> prev(n, -1);
        for (int i = 0; i < n; i++) {
            int s = events[i][0];
            int j = lower_bound(ends.begin(), ends.end(), s) - ends.begin() - 1;
            prev[i] = j;
        }

        // dp[t][i]: best using first i events (i from 0..n), taking at most t
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, 0));

        for (int t = 1; t <= k; t++) {
            for (int i = 1; i <= n; i++) {
                int skip = dp[t][i - 1];
                int take = events[i - 1][2];
                int p = prev[i - 1];
                if (p != -1) take += dp[t - 1][p + 1];
                dp[t][i] = max(skip, take);
            }
        }

        return dp[k][n];
    }
};