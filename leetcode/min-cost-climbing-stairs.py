class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int dp0 = 0; // i - 2
        int dp1 = 0; // i - 1
        for (int i = 2; i <= cost.size(); ++i) {
            int temp = dp1;
            dp1 = min(dp0 + cost[i - 2], dp1 + cost[i - 1]);
            dp0 = temp;
        }
        return dp1;
    }
};