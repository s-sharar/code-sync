class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        struct Job { int s, e, p; };
        vector<Job> jobs(n);
        for (int i = 0; i < n; i++) jobs[i] = {startTime[i], endTime[i], profit[i]};

        sort(jobs.begin(), jobs.end(), [](const Job& a, const Job& b) {
            return a.e < b.e;
        });

        vector<int> ends(n);
        for (int i = 0; i < n; i++) ends[i] = jobs[i].e;

        vector<long long> dp(n, 0);

        for (int i = 0; i < n; i++) {
            long long take = jobs[i].p;

            // p(i) = last index j < i with ends[j] <= jobs[i].s
            int j = upper_bound(ends.begin(), ends.begin() + i, jobs[i].s) - ends.begin() - 1;
            if (j >= 0) take += dp[j];

            long long skip = (i ? dp[i - 1] : 0);
            dp[i] = max(skip, take);
        }

        return (int)dp[n - 1];
    }
};