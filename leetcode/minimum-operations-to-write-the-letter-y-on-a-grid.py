class Solution {
public:
    int minimumOperationsToWriteY(vector<vector<int>>& grid) {
        int n = (int)grid.size();
        int mid = n / 2;

        long long cntY[3] = {0, 0, 0};
        long long cntN[3] = {0, 0, 0};
        long long Ysz = 0, Nsz = 0;

        auto isY = [&](int r, int c) -> bool {
            if (r <= mid && (c == r || c == n - 1 - r)) return true;
            if (r >= mid && c == mid) return true;
            return false;
        };

        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                int v = grid[r][c]; // 0,1,2
                if (isY(r, c)) {
                    cntY[v]++;
                    Ysz++;
                } else {
                    cntN[v]++;
                    Nsz++;
                }
            }
        }

        long long best = (1LL<<60);
        for (int a = 0; a < 3; ++a) {
            for (int b = 0; b < 3; ++b) {
                if (a == b) continue;
                long long ops = (Ysz - cntY[a]) + (Nsz - cntN[b]);
                if (ops < best) best = ops;
            }
        }
        return (int)best;
    }
};