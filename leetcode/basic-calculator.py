class Solution {
public:
    int calculate(string s) {
        long long res = 0;
        long long num = 0;
        int sign = 1; // +1 or -1

        vector<long long> st; // store: [prevRes, prevSign, prevRes, prevSign, ...]

        for (int i = 0; i < (int)s.size(); ++i) {
            char c = s[i];

            if (isdigit(c)) {
                num = num * 10 + (c - '0');
            } 
            else if (c == '+' || c == '-') {
                res += sign * num;
                num = 0;
                sign = (c == '+') ? 1 : -1;
            } 
            else if (c == '(') {
                // push current context
                st.push_back(res);
                st.push_back(sign);
                // reset for inside parentheses
                res = 0;
                num = 0;
                sign = 1;
            } 
            else if (c == ')') {
                // finish the number inside parens first
                res += sign * num;
                num = 0;

                int prevSign = (int)st.back(); st.pop_back();
                long long prevRes = st.back(); st.pop_back();

                res = prevRes + (long long)prevSign * res;
            }
            // spaces: ignore
        }

        // last pending number
        res += sign * num;
        return (int)res;
    }
};