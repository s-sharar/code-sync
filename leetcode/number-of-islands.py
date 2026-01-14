class Solution {
    int m, n;
    void dfs(vector<vector<char>>& g, int r, int c) {
        if (r < 0 || r >= m || c < 0 || c >= n || g[r][c] != '1') return;
        g[r][c] = '0'; // mark visited (sink)
        dfs(g, r + 1, c);
        dfs(g, r - 1, c);
        dfs(g, r, c + 1);
        dfs(g, r, c - 1);
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        m = (int)grid.size();
        n = (int)grid[0].size();
        int ans = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    ++ans;
                    dfs(grid, i, j);
                }
            }
        }
        return ans;
    }
};