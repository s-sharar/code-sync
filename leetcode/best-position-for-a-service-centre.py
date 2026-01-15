class Solution {
public:
    double getMinDistSum(vector<vector<int>>& pos) {
        int n = (int)pos.size();
        if (n == 1) return 0.0;

        double x = 0, y = 0;
        for (auto &p : pos) { x += p[0]; y += p[1]; }
        x /= n; y /= n;

        for (int it = 0; it < 500; ++it) {
            double numX = 0, numY = 0, den = 0;

            for (auto &p : pos) {
                double dx = x - p[0], dy = y - p[1];
                double d = sqrt(dx*dx + dy*dy);

                if (d < 1e-12) continue;     // avoid 1/0 blow-up
                double w = 1.0 / d;

                numX += w * p[0];
                numY += w * p[1];
                den  += w;
            }

            if (den == 0) break; // we're on top of points (or all identical)

            double nx = numX / den;
            double ny = numY / den;

            if (hypot(nx - x, ny - y) < 1e-7) { x = nx; y = ny; break; }
            x = nx; y = ny;
        }

        double ans = 0;
        for (auto &p : pos) {
            double dx = x - p[0], dy = y - p[1];
            ans += sqrt(dx*dx + dy*dy);
        }
        return ans;
    }
};