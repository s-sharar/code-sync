class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m == 0) return false;
        int n = matrix[0].size();

        int r = 0, c = n - 1;
        while (r < m && c >= 0) {
            int x = matrix[r][c];
            if (x == target) return true;
            if (x > target) c--;
            else r++;
        }
        return false;
    }
};