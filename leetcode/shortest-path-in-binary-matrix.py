class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = (int)grid.size();
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
        if (n == 1) return 1;

        static int dr[8] = {-1,-1,-1, 0,0, 1,1,1};
        static int dc[8] = {-1, 0, 1,-1,1,-1,0,1};

        queue<pair<int,int>> q;
        q.push({0,0});
        grid[0][0] = 1; // mark visited (reuse grid)

        int dist = 1;
        while (!q.empty()) {
            int sz = (int)q.size();
            dist++;
            while (sz--) {
                auto [r,c] = q.front(); q.pop();
                for (int k = 0; k < 8; k++) {
                    int nr = r + dr[k], nc = c + dc[k];
                    if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                    if (grid[nr][nc] != 0) continue; // blocked or already visited
                    if (nr == n-1 && nc == n-1) return dist;
                    grid[nr][nc] = 1;
                    q.push({nr,nc});
                }
            }
        }
        return -1;
    }
};