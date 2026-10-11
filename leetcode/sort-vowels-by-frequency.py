class Solution {
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'o' || c == 'i' || c == 'u';
    }
public:
    string sortVowels(string s) {
        string ret;
        unordered_map<char, pair<int, int>> cnt;
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            if (isVowel(c)) {
                if (!cnt.count(c)) {
                    cnt[c] = {1, i};
                } else {
                    cnt[c].first++;
                }
            }
        }
        auto cmp = [](const tuple<int, int, char> &a, const tuple<int, int, char> &b) {
            const auto &[cA, iA, _] = a;
            const auto &[cB, iB, _] = b;
            if (cA != cB) return cA < cB;
            return iA > iB;
        };
        priority_queue<tuple<int, int, char>, vector<tuple<int, int, char>>, decltype(cmp)> pq;
        for (const auto &[c, p] : cnt) {
            pq.push({p.first, p.second, c});
        }

        if (pq.empty()) return s;
        auto [count, _, c] = pq.top();
        for (char ch : s) {
            if (count == 0) {
                pq.pop();
                if (!pq.empty()) {
                    count = get<0>(pq.top());
                    c = get<2>(pq.top());
                }
            }
            if (isVowel(ch)) {
                ret += c;
                count--;
            } else ret += ch;
        }
        return ret;

    }
};