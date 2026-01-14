class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int m = (int)mat.size();
        int n = (int)mat[0].size();

        unordered_map<int, pair<int,int>> pos;
        pos.reserve(m * n * 2);

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                pos[mat[r][c]] = {r, c};
            }
        }

        vector<int> rowCount(m, 0), colCount(n, 0);

        for (int i = 0; i < (int)arr.size(); ++i) {
            auto [r, c] = pos[arr[i]];
            if (++rowCount[r] == n) return i;
            if (++colCount[c] == m) return i;
        }

        return -1; // should never happen per constraints
    }
};