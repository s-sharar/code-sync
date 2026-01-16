class Solution {
public:
    int maxArea(vector<int>& h) {
        int l = 0, r = (int)h.size() - 1;
        long long best = 0;
        while (l < r) {
            long long width = r - l;
            long long height = min(h[l], h[r]);
            best = max(best, width * height);
            if (h[l] <= h[r]) l++;
            else r--;
        }
        return (int)best;
    }
};