class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int n = (int)A.size(), m = (int)B.size();
        vector<int> dp(m + 1, 0);
        int ans = 0;

        for (int i = 1; i <= n; ++i) {
            for (int j = m; j >= 1; --j) { // go backwards so dp[j-1] is from prev row
                if (A[i - 1] == B[j - 1]) dp[j] = dp[j - 1] + 1;
                else dp[j] = 0;
                ans = max(ans, dp[j]);
            }
        }
        return ans;
    }
};