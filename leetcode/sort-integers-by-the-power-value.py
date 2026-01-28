class Solution {
public:
    int getKth(int lo, int hi, int k) {
        unordered_map<long long, int> memo;
        memo[1] = 0;

        function<int(long long)> power = [&](long long x) -> int {
            if (memo.count(x)) return memo[x];
            int ans;
            if (x % 2 == 0) ans = 1 + power(x / 2);
            else ans = 1 + power(3 * x + 1);
            memo[x] = ans;
            return ans;
        };

        vector<pair<int,int>> v;
        v.reserve(hi - lo + 1);
        for (int x = lo; x <= hi; x++) {
            v.push_back({power(x), x});
        }

        sort(v.begin(), v.end());              // sorts by power, then x automatically
        return v[k - 1].second;
    }
};