class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = (int)obstacleGrid.size();
        int n = (int)obstacleGrid[0].size();

        vector<long long> dp(n, 0);

        // start cell
        dp[0] = (obstacleGrid[0][0] == 1) ? 0 : 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;                 // can't stand on obstacle
                } else if (j > 0) {
                    dp[j] = dp[j] + dp[j - 1]; // top (dp[j]) + left (dp[j-1])
                }
                // else j==0 and not obstacle: dp[0] stays as "from top only"
            }
        }
        return (int)dp[n - 1];
    }
};