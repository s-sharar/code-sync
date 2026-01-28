class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int,int> cnt;
        int rows = (int)wall.size();
        int best = 0;

        for (auto &row : wall) {
            long long x = 0;
            // stop before last brick so we don't count the right boundary
            for (int i = 0; i < (int)row.size() - 1; i++) {
                x += row[i];
                best = max(best, ++cnt[x]);
            }
        }
        return rows - best;
    }
};