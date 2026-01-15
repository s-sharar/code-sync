class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int lo = 1;
        int hi = *max_element(piles.begin(), piles.end());

        auto can = [&](int k) -> bool {
            long long hours = 0;
            for (int p : piles) {
                hours += (p + k - 1) / k; // ceil(p/k)
                if (hours > h) return false;
            }
            return hours <= h;
        };

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};