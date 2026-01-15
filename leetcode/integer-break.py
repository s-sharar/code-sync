class Solution {
public:
    int integerBreak(int n) {
        if (n == 2) return 1;
        if (n == 3) return 2;

        long long res = 1;
        while (n > 4) { // keep n in {2,3,4} at end
            res *= 3;
            n -= 3;
        }
        res *= n; // n is 2,3, or 4
        return (int)res;
    }
};