class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2) return 0;

        vector<char> isPrime(n, true);
        isPrime[0] = isPrime[1] = false;

        for (long long i = 2; i * i < n; ++i) {
            if (!isPrime[i]) continue;
            for (long long j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }

        int cnt = 0;
        for (int i = 2; i < n; ++i) cnt += isPrime[i];
        return cnt;
    }
};