class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        vector<string> board(n, string(n, '.'));

        vector<int> col(n, 0);
        vector<int> diag1(2*n - 1, 0); // r - c + (n-1)
        vector<int> diag2(2*n - 1, 0); // r + c

        function<void(int)> dfs = [&](int r) {
            if (r == n) {
                ans.push_back(board);
                return;
            }
            for (int c = 0; c < n; c++) {
                int d1 = r - c + (n - 1);
                int d2 = r + c;
                if (col[c] || diag1[d1] || diag2[d2]) continue;

                col[c] = diag1[d1] = diag2[d2] = 1;
                board[r][c] = 'Q';

                dfs(r + 1);

                board[r][c] = '.';
                col[c] = diag1[d1] = diag2[d2] = 0;
            }
        };

        dfs(0);
        return ans;
    }
};