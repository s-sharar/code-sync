class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        string lexSmallest = strs[0];
        string lexLargest  = strs[0];

        for (const string& s : strs) {
            if (s < lexSmallest) lexSmallest = s;
            if (s > lexLargest)  lexLargest  = s;
        }

        int i = 0;
        int limit = (int)min(lexSmallest.size(), lexLargest.size());
        while (i < limit && lexSmallest[i] == lexLargest[i]) {
            i++;
        }
        return lexSmallest.substr(0, i);
    }
};