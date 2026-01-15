class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        const int MOD = 1'000'000'007;
        vector<int> prev(target + 1, 0), cur(target + 1, 0);
        prev[0] = 1;

        for (int i = 1; i <= n; i++) {
            fill(cur.begin(), cur.end(), 0);
            long long window = 0; // sum of prev[s-1]..prev[s-k]
            for (int s = 1; s <= target; s++) {
                window += prev[s - 1];
                if (s - k - 1 >= 0) window -= prev[s - k - 1];
                window %= MOD;
                if (window < 0) window += MOD;
                cur[s] = (int)window;
            }
            prev.swap(cur);
        }
        return prev[target];
    }
};