#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int, int> cnt;
        cnt.reserve(power.size() * 2);

        for (int x : power) ++cnt[x];

        vector<int> vals;
        vals.reserve(cnt.size());
        for (auto& [v, c] : cnt) vals.push_back(v);
        sort(vals.begin(), vals.end());

        int m = (int)vals.size();
        vector<long long> gain(m);
        for (int i = 0; i < m; ++i) {
            long long v = vals[i];
            gain[i] = v * (long long)cnt[vals[i]];
        }

        vector<long long> dp(m, 0);
        for (int i = 0; i < m; ++i) {
            long long take = gain[i];

            // prev index with vals[prev] <= vals[i] - 3
            int target = vals[i] - 3;
            int j = int(upper_bound(vals.begin(), vals.begin() + i, target) - vals.begin()) - 1;
            if (j >= 0) take += dp[j];

            long long skip = (i ? dp[i - 1] : 0);
            dp[i] = max(skip, take);
        }

        return dp.empty() ? 0 : dp.back();
    }
};