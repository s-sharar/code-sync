class Solution {
public:
    bool isMatch(string s, string p) {
        int n = (int)s.size(), m = (int)p.size();
        vector<vector<char>> dp(n + 1, vector<char>(m + 1, false));
        dp[0][0] = true;

        // empty
        for (int j = 2; j <= m; ++j)
            if (p[j - 1] == '*')
                dp[0][j] = dp[0][j - 2];

        auto charMatch = [&](int i, int j) {
            return i > 0 && (p[j - 1] == '.' || p[j - 1] == s[i - 1]);
        };

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (p[j - 1] != '*') {
                    dp[i][j] = charMatch(i, j) && dp[i - 1][j - 1];
                } else {
                    // zero occurrences
                    dp[i][j] = dp[i][j - 2];

                    // one or more occurrences
                    if (j >= 2 && (p[j - 2] == '.' || p[j - 2] == s[i - 1]))
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                }
            }
        }
        return dp[n][m];
    }
};