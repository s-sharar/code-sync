class Solution {
public:
    int trap(vector<int>& heights) {
        int l = 0, r = (int)heights.size() - 1;
        int leftMax = 0, rightMax = 0;
        int res = 0;

        while (l <= r) {
            if (leftMax <= rightMax) {
                leftMax = max(leftMax, heights[l]);
                res += leftMax - heights[l];
                ++l;
            } else {
                rightMax = max(rightMax, heights[r]);
                res += rightMax - heights[r];
                --r;
            }
        }
        return res;
    }
};