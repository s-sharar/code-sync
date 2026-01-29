class StockSpanner {
    // stack: prices strictly decreasing, each with its computed span
    vector<pair<int,int>> st; // (price, span)

public:
    StockSpanner() {}

    int next(int price) {
        int span = 1;
        while (!st.empty() && st.back().first <= price) {
            span += st.back().second; // absorb spans
            st.pop_back();
        }
        st.push_back({price, span});
        return span;
    }
};