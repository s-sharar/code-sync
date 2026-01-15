class Solution {
public:
    vector<int> asteroidCollision(vector<int>& ast) {
        vector<int> st;
        for (int a : ast) {
            bool alive = true;
            while (alive && a < 0 && !st.empty() && st.back() > 0) {
                if (st.back() < -a) st.pop_back();       // right one dies
                else if (st.back() == -a) { st.pop_back(); alive = false; } // both die
                else alive = false;                      // a dies
            }
            if (alive) st.push_back(a);
        }
        return st;
    }
};