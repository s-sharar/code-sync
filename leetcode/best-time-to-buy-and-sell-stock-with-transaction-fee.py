class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        long long hold = INT_MIN;
        long long notHold = 0;
        for (int price : prices) {
            long long nhold = max(hold, notHold - price);
            long long nnotHold = max(nnotHold, hold + price - fee);
            hold = nhold;
            notHold = nnotHold;
        }
        return notHold;
    }
};