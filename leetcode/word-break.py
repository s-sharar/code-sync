class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> dp(n + 1, false);
        dp[0] = true;
        for (int i = 1; i <= n; ++i) {
            for (const string &word : wordDict) {
                if (i - 1 + word.size() <= n && word == s.substr(i - 1, word.size())) dp[i - 1 + word.size()] = dp[i - 1 + word.size()] || dp[i - 1];
            }
        }
        return dp[n];
    }
};