class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int,int> cnt;
        for (int x: power) cnt[x]++;

        vector<int> vals;
        vals.reserve(cnt.size());
        for (auto &p: cnt) vals.push_back(p.first);
        sort(vals.begin(), vals.end());

        int m = vals.size();
        vector<long long> gain(m);
        for (int i = 0; i < m; ++i) gain[i] = 1LL * vals[i] * cnt[vals[i]];

        vector<long long> dp(m, 0);
        int j = 0; // first index that conflicts with i (>= vals[i]-2)

        for (int i = 0; i < m; ++i) {
            while (j < i && vals[j] <= vals[i] - 3) j++; 
            // now j is first index with vals[j] > vals[i]-3
            int prev = j - 1; // last index <= vals[i]-3

            long long take = gain[i] + (prev >= 0 ? dp[prev] : 0);
            long long skip = (i ? dp[i-1] : 0);
            dp[i] = max(skip, take);
        }
        return m ? dp[m-1] : 0;
    }

};