class Solution {
public:
    int superEggDrop(int K, int N) {
        vector<long long> prev(K+1, 0), cur(K+1, 0);
        int m = 0;
        while (prev[K] < N) {
            m++;
            cur[0] = 0;
            for (int e = 1; e <= K; ++e) {
                cur[e] = prev[e] + prev[e-1] + 1;
            }
            swap(prev, cur);
        }
        return m;
    }

};