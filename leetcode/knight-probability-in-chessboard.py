class Solution {
public:
    double knightProbability(int n, int k, int row, int column) {
        vector<pair<int, int>> moves = {
            {2, 1}, {2, -1}, {-2, 1}, {-2, -1},
            {1, 2}, {1, -2}, {-1, 2}, {-1, -2}
        };

        vector<vector<double>> dp(n, vector<double>(n, 0));
        dp[row][column] = 1.0;

        for (int move = 0; move < k; move++) {
            vector<vector<double>> next(n, vector<double>(n, 0));

            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    for (auto [dr, dc] : moves) {
                        int nr = r + dr;
                        int nc = c + dc;

                        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                            next[nr][nc] += dp[r][c] / 8.0;
                        }
                    }
                }
            }

            dp = next;
        }

        double answer = 0;

        for (const auto& boardRow : dp) {
            for (double probability : boardRow) {
                answer += probability;
            }
        }

        return answer;
    }
};