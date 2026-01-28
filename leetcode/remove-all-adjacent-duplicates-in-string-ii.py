class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char,int>> st; // acts like a stack: {char, count}

        for (char c : s) {
            if (st.empty() || st.back().first != c) {
                st.push_back({c, 1});
            } else {
                st.back().second++;
                if (st.back().second == k) {
                    st.pop_back(); // remove the k duplicates
                }
            }
        }

        // Build answer in correct order
        string ans;
        for (auto &p : st) {
            ans.append(p.second, p.first); // append count copies of char
        }
        return ans;
    }
};