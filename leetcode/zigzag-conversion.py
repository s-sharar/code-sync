class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1 || (int)s.size() <= numRows) return s;

        vector<string> rows(numRows);
        int cur = 0;
        int dir = +1; // +1 = going down, -1 = going up

        for (char c : s) {
            rows[cur].push_back(c);

            // bounce at the ends
            if (cur == 0) dir = +1;
            else if (cur == numRows - 1) dir = -1;

            cur += dir;
        }

        string ans;
        ans.reserve(s.size());
        for (auto &r : rows) ans += r;
        return ans;
    }
};