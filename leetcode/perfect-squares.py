class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, 1e9);
        dp[0] = 0;

        for (int x = 1; x <= n; ++x) {
            for (int i = 1; i * i <= x; ++i) {
                dp[x] = min(dp[x], dp[x - i*i] + 1);
            }
        }
        return dp[n];
    }
};