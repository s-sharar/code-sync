class Solution {
public:
    string decodeString(string s) {
        stack<pair<string,int>> st;
        string curr;
        int num = 0;

        for (char c : s) {
            if (isdigit(c)) {
                num = num * 10 + (c - '0');
            } else if (c == '[') {
                st.push({curr, num});
                curr.clear();
                num = 0;
            } else if (c == ']') {
                auto [prev, k] = st.top();
                st.pop();

                string repeated;
                repeated.reserve(curr.size() * k);
                for (int i = 0; i < k; i++) repeated += curr;

                curr = prev + repeated;
            } else { // letter
                curr.push_back(c);
            }
        }
        return curr;
    }
};