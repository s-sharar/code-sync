class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = INT_MAX;
        int maxProf = 0;
        for (int price : prices) {
            if (price < buy) {
                buy = price;
            }
            maxProf = max(maxProf, price - buy);
        }
        return maxProf;
    }
};