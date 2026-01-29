class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int best = A[0] + 0;
        int ans = INT_MIN;

        for (int j = 1; j < (int)A.size(); j++) {
            ans = max(ans, best + A[j] - j);
            best = max(best, A[j] + j);
        }
        return ans;
    }
};