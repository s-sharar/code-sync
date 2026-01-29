class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        unordered_map<int,int> c1, c2;
        int mn = INT_MAX;

        for (int x : basket1) c1[x]++, mn = min(mn, x);
        for (int x : basket2) c2[x]++, mn = min(mn, x);

        vector<int> A, B;

        // check feasibility + build diffs
        unordered_set<int> keys;
        for (auto &p : c1) keys.insert(p.first);
        for (auto &p : c2) keys.insert(p.first);

        for (int x : keys) {
            int a = c1[x], b = c2[x];
            if ( (a + b) % 2 ) return -1;

            if (a > b) {
                int k = (a - b) / 2;
                while (k--) A.push_back(x);
            } else if (b > a) {
                int k = (b - a) / 2;
                while (k--) B.push_back(x);
            }
        }

        sort(A.begin(), A.end());
        sort(B.begin(), B.end(), greater<int>());

        long long ans = 0;
        for (int i = 0; i < (int)A.size(); i++) {
            ans += min((long long)min(A[i], B[i]), 2LL * mn);
        }
        return ans;
    }
};