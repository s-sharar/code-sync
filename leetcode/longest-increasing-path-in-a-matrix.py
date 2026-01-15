class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

        function<int(int,int)> dfs = [&](int r, int c) -> int {
            if (dp[r][c]) return dp[r][c];

            int best = 1; // at least the cell itself
            for (auto &d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (matrix[nr][nc] <= matrix[r][c]) continue; // must increase
                best = max(best, 1 + dfs(nr, nc));
            }
            return dp[r][c] = best;
        };

        int ans = 0;
        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c)
                ans = max(ans, dfs(r, c));

        return ans;
    }
};