class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = (int)points.size();
        if (n <= 2) return n;

        int ans = 0;

        for (int i = 0; i < n; ++i) {
            unordered_map<long long, int> cnt;
            cnt.reserve(n * 2);

            int dup = 0;
            int best = 0;

            long long xi = points[i][0], yi = points[i][1];

            for (int j = i + 1; j < n; ++j) {
                long long dx = (long long)points[j][0] - xi;
                long long dy = (long long)points[j][1] - yi;

                if (dx == 0 && dy == 0) { // duplicate point
                    dup++;
                    continue;
                }

                // reduce by gcd
                long long adx = llabs(dx), ady = llabs(dy);
                long long g = std::gcd(adx, ady);
                dx /= g; dy /= g;

                // canonicalize sign / special cases
                if (dx == 0) {
                    dy = 1;              // all vertical => (0,1)
                } else if (dy == 0) {
                    dx = 1;              // all horizontal => (1,0)
                } else if (dx < 0) {
                    dx = -dx; dy = -dy;  // keep dx positive
                }

                // pack (dx, dy) into one 64-bit key
                // offset dy to avoid collisions with negatives
                const long long OFF = 200000; // safe because reduced dx,dy are within ~[-2e4,2e4]
                long long key = (dx << 32) ^ (dy + OFF);

                best = max(best, ++cnt[key]);
            }

            // +1 for anchor itself, +dup for duplicates at anchor
            ans = max(ans, best + dup + 1);
        }

        return ans;
    }
};