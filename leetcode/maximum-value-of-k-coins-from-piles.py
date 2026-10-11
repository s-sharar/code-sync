class Solution {
    static constexpr int NEG = -1000000000;
    vector<vector<int>> memo;

    int solve(int i, int remaining, vector<vector<int>>& piles) {
        if (remaining == 0) return 0;
        if (i == piles.size()) return NEG; // Can't take enough coins

        int& ans = memo[i][remaining];
        if (ans != -1) return ans;

        // Take 0 coins from this pile
        ans = solve(i + 1, remaining, piles);

        int sum = 0;
        int limit = min(remaining, (int)piles[i].size());

        for (int take = 1; take <= limit; take++) {
            sum += piles[i][take - 1];

            int rest = solve(i + 1, remaining - take, piles);
            if (rest != NEG) {
                ans = max(ans, sum + rest);
            }
        }

        return ans;
    }

public:
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        memo.assign(piles.size(), vector<int>(k + 1, -1));
        return solve(0, k, piles);
    }
};