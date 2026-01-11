class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n = (int)grid.size();
        vector<long long> prev(n), curr(n);

        for (int c = 0; c < n; c++) prev[c] = grid[0][c];

        for (int r = 1; r < n; r++) {
            // find smallest and second smallest in prev
            long long min1 = LLONG_MAX, min2 = LLONG_MAX;
            int idx1 = -1;
            for (int c = 0; c < n; c++) {
                long long v = prev[c];
                if (v < min1) {
                    min2 = min1;
                    min1 = v;
                    idx1 = c;
                } else if (v < min2) {
                    min2 = v;
                }
            }

            for (int c = 0; c < n; c++) {
                long long bestPrev = (c == idx1 ? min2 : min1);
                curr[c] = bestPrev + grid[r][c];
            }

            prev.swap(curr);
        }

        return (int)*min_element(prev.begin(), prev.end());
    }
};