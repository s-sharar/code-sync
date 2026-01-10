class Solution {
    bool canPlace(const vector<int>& pos, int m, int d) {
        int placed = 1;
        int last = pos[0];
        for (int i = 1; i < (int)pos.size(); ++i) {
            if (pos[i] - last >= d) {
                placed++;
                last = pos[i];
                if (placed >= m) return true;
            }
        }
        return false;
    }

public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        int lo = 1;
        int hi = position.back() - position.front(); // max possible min distance
        int ans = 0;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (canPlace(position, m, mid)) {
                ans = mid;       // mid works, try bigger
                lo = mid + 1;
            } else {
                hi = mid - 1;    // mid too big
            }
        }
        return ans;
    }
};