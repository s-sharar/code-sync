class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0); // sentinel to flush stack
        vector<int> st;       // stack of indices (increasing heights)
        long long best = 0;

        for (int i = 0; i < (int)heights.size(); i++) {
            while (!st.empty() && heights[st.back()] > heights[i]) {
                int mid = st.back();
                st.pop_back();

                int leftSmaller = st.empty() ? -1 : st.back();
                int rightSmaller = i;
                long long width = rightSmaller - leftSmaller - 1;
                best = max(best, width * heights[mid]);
            }
            st.push_back(i);
        }

        heights.pop_back(); // optional cleanup
        return (int)best;
    }
};