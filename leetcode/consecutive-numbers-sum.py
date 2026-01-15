class Solution {
public:
    int consecutiveNumbersSum(int n) {
        long long N = n;
        int ways = 0;

        for (long long k = 1; k * (k + 1) / 2 <= N; ++k) {
            // n = a + (a+1) + ... + (a+k-1)
            // => n = k*a + k(k-1)/2
            // => a = (n - k(k-1)/2) / k
            long long numer = N - k * (k - 1) / 2;
            if (numer > 0 && numer % k == 0) ways++;
        }

        return ways;
    }
};