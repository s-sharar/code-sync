class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

        function<bool(int,int,int)> dfs = [&](int r, int c, int k) -> bool {
            if (board[r][c] != word[k]) return false;
            if (k == (int)word.size() - 1) return true;

            char saved = board[r][c];
            board[r][c] = '#'; // mark used

            for (auto &d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (board[nr][nc] == '#') continue;
                if (dfs(nr, nc, k + 1)) {
                    board[r][c] = saved;
                    return true;
                }
            }

            board[r][c] = saved; // unmark
            return false;
        };

        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c)
                if (dfs(r, c, 0)) return true;

        return false;
    }
};