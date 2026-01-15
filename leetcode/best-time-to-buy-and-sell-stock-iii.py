class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy1  = INT_MIN;  // max(-price)
        int sell1 = 0;        // max profit after 1 sell
        int buy2  = INT_MIN;  // max(sell1 - price)
        int sell2 = 0;        // max profit after 2 sells

        for (int p : prices) {
            buy1  = max(buy1, -p);        // buy first stock
            sell1 = max(sell1, buy1 + p); // sell first stock
            buy2  = max(buy2, sell1 - p); // buy second stock
            sell2 = max(sell2, buy2 + p); // sell second stock
        }
        return sell2;
    }
};