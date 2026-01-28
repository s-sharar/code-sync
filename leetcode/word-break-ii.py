class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        int n = (int)s.size();

        // Optional speed-up: limit max word length so we don't try all j up to n
        int maxLen = 0;
        for (auto &w : wordDict) maxLen = max(maxLen, (int)w.size());

        vector<char> vis(n + 1, 0);
        vector<vector<string>> memo(n + 1);

        function<vector<string>&(int)> dfs = [&](int i) -> vector<string>& {
            if (vis[i]) return memo[i];
            vis[i] = 1;

            vector<string> res;

            // Base case: reached end => one valid "empty sentence"
            if (i == n) {
                res.push_back("");
                memo[i] = std::move(res);
                return memo[i];
            }

            int limit = min(n, i + maxLen);
            for (int j = i + 1; j <= limit; j++) {
                string word = s.substr(i, j - i);
                if (!dict.count(word)) continue;

                // Get all sentences for the suffix starting at j
                vector<string>& tails = dfs(j);

                // Attach current word in front of each suffix sentence
                for (string &tail : tails) {
                    if (tail.empty()) res.push_back(word);
                    else res.push_back(word + " " + tail);
                }
            }

            memo[i] = std::move(res);
            return memo[i];
        };

        return dfs(0);
    }
};