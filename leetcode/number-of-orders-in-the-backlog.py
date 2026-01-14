class Solution {
public:
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        const int MOD = 1'000'000'007;

        // buy: max price first
        priority_queue<pair<int,int>> buy; 
        // sell: min price first
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> sell;

        for (auto &o : orders) {
            int price = o[0];
            int amount = o[1];
            int type = o[2];

            if (type == 0) { // buy
                while (amount > 0 && !sell.empty() && sell.top().first <= price) {
                    auto [sp, sa] = sell.top(); sell.pop();
                    int m = min(amount, sa);
                    amount -= m;
                    sa -= m;
                    if (sa > 0) sell.push({sp, sa});
                }
                if (amount > 0) buy.push({price, amount});
            } else { // sell
                while (amount > 0 && !buy.empty() && buy.top().first >= price) {
                    auto [bp, ba] = buy.top(); buy.pop();
                    int m = min(amount, ba);
                    amount -= m;
                    ba -= m;
                    if (ba > 0) buy.push({bp, ba});
                }
                if (amount > 0) sell.push({price, amount});
            }
        }

        long long ans = 0;
        while (!buy.empty()) {
            ans = (ans + buy.top().second) % MOD;
            buy.pop();
        }
        while (!sell.empty()) {
            ans = (ans + sell.top().second) % MOD;
            sell.pop();
        }
        return (int)ans;
    }
};