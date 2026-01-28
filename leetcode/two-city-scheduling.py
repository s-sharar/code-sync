class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int n2 = (int)costs.size();
        int n = n2 / 2;

        long long base = 0;
        vector<int> delta;
        delta.reserve(n2);

        for (auto &c : costs) {
            base += c[0];                 // everyone to A
            delta.push_back(c[1] - c[0]); // extra if send to B instead
        }

        nth_element(delta.begin(), delta.begin() + n, delta.end());
        long long ans = base;
        for (int i = 0; i < n; i++) ans += delta[i];

        return (int)ans;
    }
};