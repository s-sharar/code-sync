class Solution {
    vector<string> ans;

    const vector<string> letters = {
        "",     // 0
        "",     // 1
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz"  // 9
    };

    void dfs(const string& digits, int i, string& curr) {
        // Chose one letter for every digit
        if (i == digits.size()) {
            ans.push_back(curr);
            return;
        }

        int digit = digits[i] - '0';

        for (char ch : letters[digit]) {
            curr.push_back(ch);          // choose
            dfs(digits, i + 1, curr);    // solve rest
            curr.pop_back();             // undo
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        string curr;
        dfs(digits, 0, curr);

        return ans;
    }
};