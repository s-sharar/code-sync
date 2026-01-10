class Solution {
public:
    vector<long long> countBlackBlocks(int m, int n, vector<vector<int>>& coordinates) {
        unordered_map<long long, int> cnt;
        cnt.reserve(coordinates.size() * 4);

        auto key = [](int r, int c) -> long long {
            // pack (r,c) into one 64-bit key
            return ( (long long)r << 32 ) ^ (unsigned int)c;
        };

        for (auto &p : coordinates) {
            int r = p[0], c = p[1];

            // top-left candidates
            for (int dr = -1; dr <= 0; ++dr) {
                for (int dc = -1; dc <= 0; ++dc) {
                    int tr = r + dr;
                    int tc = c + dc;
                    if (tr >= 0 && tr < m - 1 && tc >= 0 && tc < n - 1) {
                        cnt[key(tr, tc)]++;
                    }
                }
            }
        }

        vector<long long> ans(5, 0);
        for (auto &it : cnt) {
            int k = it.second;          // 1..4
            ans[k]++;
        }

        long long total = 1LL * (m - 1) * (n - 1);
        long long nonzero = ans[1] + ans[2] + ans[3] + ans[4];
        ans[0] = total - nonzero;

        return ans;
    }
};