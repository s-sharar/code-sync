class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x;              // 0 -> 0, 1 -> 1

        int lo = 1, hi = x / 2;           // sqrt(x) <= x/2 for x>=2
        int ans = 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (mid <= x / mid) {         // mid*mid <= x, but no overflow
                ans = mid;                // mid works; try bigger
                lo = mid + 1;
            } else {
                hi = mid - 1;             // mid too big
            }
        }
        return ans;
    }
};