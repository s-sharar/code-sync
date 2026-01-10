class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        unordered_map<string, int> freq;
        vector<int> count(26, 0);

        int distinct = 0;
        int best = 0;

        int n = (int)s.size();
        for (int r = 0; r < n; ++r) {
            int in = s[r] - 'a';
            if (count[in]++ == 0) distinct++;

            // shrink to keep window size == minSize
            if (r >= minSize) {
                int out = s[r - minSize] - 'a';
                if (--count[out] == 0) distinct--;
            }

            if (r >= minSize - 1) {
                if (distinct <= maxLetters) {
                    string key = s.substr(r - minSize + 1, minSize);
                    int newCount = ++freq[key];
                    if (newCount > best) best = newCount;
                }
            }
        }
        return best;
    }
};