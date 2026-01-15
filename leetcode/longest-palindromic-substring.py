class Solution {
public:
    string longestPalindrome(string s) {
        int n = (int)s.size();
        if (n <= 1) return s;

        int bestL = 0, bestLen = 1;

        auto expand = [&](int l, int r) {
            while (l >= 0 && r < n && s[l] == s[r]) {
                l--; r++;
            }
            // went one step too far
            int len = r - l - 1;
            int start = l + 1;
            if (len > bestLen) {
                bestLen = len;
                bestL = start;
            }
        };

        for (int i = 0; i < n; i++) {
            expand(i, i);     // odd
            expand(i, i + 1); // even
        }
        return s.substr(bestL, bestLen);
    }
};