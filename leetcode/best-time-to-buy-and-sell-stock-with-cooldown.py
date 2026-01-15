class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int hold = INT_MIN;   // holding a stock
        int sold = INT_MIN;   // sold today
        int rest = 0;         // not holding, not sold today

        for (int p : prices) {
            int new_hold = max(hold, rest - p);
            int new_sold = hold + p;
            int new_rest = max(rest, sold);

            hold = new_hold;
            sold = new_sold;
            rest = new_rest;
        }
        return max(rest, sold); // best profit not holding at the end
    }
};