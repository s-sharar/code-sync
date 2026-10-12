class Solution {
public:
    int maxCoins(vector<int>& nums) {
        vector<int> balloons = {1};
        balloons.insert(balloons.end(), nums.begin(), nums.end());
        balloons.push_back(1);

        int size = balloons.size();
        vector<vector<int>> dp(size, vector<int>(size, 0));

        for (int gap = 2; gap < size; ++gap) {
            for (int left = 0; left + gap < size; ++left) {
                int right = left + gap;

                for (int last = left + 1; last < right; ++last) {
                    int coins =
                        dp[left][last] +
                        dp[last][right] +
                        balloons[left] * balloons[last] * balloons[right];

                    dp[left][right] = max(dp[left][right], coins);
                }
            }
        }

        return dp[0][size - 1];
    }
};