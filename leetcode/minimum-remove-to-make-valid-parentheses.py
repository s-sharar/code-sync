class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int n = (int)s.size();
        vector<char> keep(n, 1);

        int open = 0;

        // Pass 1: remove invalid ')'
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                open++;
            } else if (s[i] == ')') {
                if (open > 0) open--;
                else keep[i] = 0; // invalid closing
            }
        }

        // Pass 2: remove extra '(' from right
        for (int i = n - 1; i >= 0 && open > 0; i--) {
            if (s[i] == '(' && keep[i]) {
                keep[i] = 0;
                open--;
            }
        }

        // Build answer
        string ans;
        ans.reserve(n);
        for (int i = 0; i < n; i++) {
            if (keep[i]) ans.push_back(s[i]);
        }
        return ans;
    }
};