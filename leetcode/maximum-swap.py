class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        vector<int> last(10, -1);

        for (int i = 0; i < (int)s.size(); i++) {
            last[s[i] - '0'] = i;
        }

        for (int i = 0; i < (int)s.size(); i++) {
            int cur = s[i] - '0';
            for (int d = 9; d > cur; d--) {
                if (last[d] > i) {
                    swap(s[i], s[last[d]]);
                    return stoi(s);
                }
            }
        }
        return num;
    }
};