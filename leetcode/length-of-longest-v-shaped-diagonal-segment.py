class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();

        // dirs clockwise: ↗, ↘, ↙, ↖
        const int dx[4] = {-1,  1,  1, -1};
        const int dy[4] = { 1,  1, -1, -1};

        auto idxNeed = [&](int need) { return (need == 2) ? 1 : 0; };

        // flat memo: [i][j][dir][turned][needIdx]
        // size = m*n*4*2*2
        vector<int> memo((size_t)m * n * 16, -1);

        auto ID = [&](int i, int j, int dir, int turned, int need) -> int {
            int k = i * n + j;                 // 0..m*n-1
            int t = (((k * 4 + dir) * 2 + turned) * 2 + idxNeed(need));
            return t;                          // 0..m*n*16-1
        };

        auto dfs = [&](auto&& self, int i, int j, int dir, int turned, int need) -> int {
            if (i < 0 || i >= m || j < 0 || j >= n) return 0;
            if (grid[i][j] != need) return 0;

            int id = ID(i, j, dir, turned, need);
            int &cached = memo[id];
            if (cached != -1) return cached;

            int nextNeed = (need == 2 ? 0 : 2);

            int best = 1 + self(self, i + dx[dir], j + dy[dir], dir, turned, nextNeed);

            if (!turned) {
                int ndir = (dir + 1) % 4; // clockwise turn
                best = max(best, 1 + self(self, i + dx[ndir], j + dy[ndir], ndir, 1, nextNeed));
            }

            return cached = best;
        };

        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != 1) continue;
                ans = max(ans, 1);
                for (int dir = 0; dir < 4; ++dir) {
                    ans = max(ans, 1 + dfs(dfs, i + dx[dir], j + dy[dir], dir, 0, 2));
                }
            }
        }
        return ans;
    }
};