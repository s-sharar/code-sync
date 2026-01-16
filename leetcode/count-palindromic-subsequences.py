class Solution {
public:
    int countPalindromes(string s) {
        const int MOD = 1'000'000'007;
        int n = (int)s.size();

        // leftPairs[k][a][b] = # of "a then b" using indices < k
        // rightPairs[k][a][b] = # of "a then b" using indices > k
        vector<array<array<long long, 10>, 10>> leftPairs(n), rightPairs(n);

        // Build leftPairs
        long long cnt1[10] = {0};
        long long pair[10][10] = {{0}};
        for (int k = 0; k < n; k++) {
            // snapshot BEFORE consuming s[k]
            for (int a = 0; a < 10; a++)
                for (int b = 0; b < 10; b++)
                    leftPairs[k][a][b] = pair[a][b];

            int x = s[k] - '0';
            for (int d = 0; d < 10; d++) {
                pair[d][x] = (pair[d][x] + cnt1[d]) % MOD;
            }
            cnt1[x]++;
        }

        // Build rightPairs
        long long cnt1R[10] = {0};
        long long pairR[10][10] = {{0}};
        for (int k = n - 1; k >= 0; k--) {
            // snapshot BEFORE consuming s[k]
            for (int a = 0; a < 10; a++)
                for (int b = 0; b < 10; b++)
                    rightPairs[k][a][b] = pairR[a][b];

            int x = s[k] - '0';
            for (int d = 0; d < 10; d++) {
                pairR[x][d] = (pairR[x][d] + cnt1R[d]) % MOD;
            }
            cnt1R[x]++;
        }

        // Combine
        long long ans = 0;
        for (int k = 0; k < n; k++) {
            for (int a = 0; a < 10; a++) {
                for (int b = 0; b < 10; b++) {
                    long long L = leftPairs[k][a][b];
                    long long R = rightPairs[k][b][a];
                    ans = (ans + L * R) % MOD;
                }
            }
        }
        return (int)ans;
    }
};