class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        unordered_map<int,int> cnt;
        long long res = 0;

        for (int x : time) {
            int t = x % 60;
            int need = (60 - t) % 60;
            auto it = cnt.find(need);
            if (it != cnt.end()) res += it->second;
            cnt[t]++;
        }
        return (int)res;
    }
};