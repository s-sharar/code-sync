class Solution {
public:
    double findMedianSortedArrays(vector<int>& A, vector<int>& B) {
        if (A.size() > B.size()) return findMedianSortedArrays(B, A); // A is smaller
        int m = (int)A.size(), n = (int)B.size();

        int half = (m + n + 1) / 2;
        int lo = 0, hi = m;

        while (lo <= hi) {
            int i = (lo + hi) / 2;      // cut in A
            int j = half - i;           // cut in B

            int Aleft  = (i == 0) ? INT_MIN : A[i - 1];
            int Aright = (i == m) ? INT_MAX : A[i];
            int Bleft  = (j == 0) ? INT_MIN : B[j - 1];
            int Bright = (j == n) ? INT_MAX : B[j];

            if (Aleft <= Bright && Bleft <= Aright) {
                // correct partition
                int leftMax = max(Aleft, Bleft);
                if (((m + n) & 1) == 1) return (double)leftMax;
                int rightMin = min(Aright, Bright);
                return (leftMax + rightMin) / 2.0;
            }

            // move i
            if (Aleft > Bright) {
                hi = i - 1; // cut too far right in A
            } else {
                lo = i + 1; // cut too far left in A
            }
        }
        return 0.0; // unreachable if inputs are valid
    }
};