class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int top = 0, bottom = m - 1, left = 0, right = n - 1;
        vector<int> res;
        res.reserve(m * n);

        while (top <= bottom && left <= right) {
            // top row
            for (int j = left; j <= right; ++j) res.push_back(matrix[top][j]);
            ++top;
            if (top > bottom) break;

            // right col
            for (int i = top; i <= bottom; ++i) res.push_back(matrix[i][right]);
            --right;
            if (left > right) break;

            // bottom row
            for (int j = right; j >= left; --j) res.push_back(matrix[bottom][j]);
            --bottom;
            if (top > bottom) break;

            // left col
            for (int i = bottom; i >= top; --i) res.push_back(matrix[i][left]);
            ++left;
        }
        return res;
    }
};