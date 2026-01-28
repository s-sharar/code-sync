class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        int n = (int)nums.size();
        vector<int> ans;

        for (int i = 0; i + k <= n; i++) {
            unordered_map<int,int> freq;
            for (int j = i; j < i + k; j++) freq[nums[j]]++;

            // If distinct < x => sum entire window
            if ((int)freq.size() < x) {
                int s = 0;
                for (int j = i; j < i + k; j++) s += nums[j];
                ans.push_back(s);
                continue;
            }

            // Sort by (freq desc, value desc)
            vector<pair<int,int>> items; // (value, freq)
            items.reserve(freq.size());
            for (auto &p : freq) items.push_back({p.first, p.second});

            sort(items.begin(), items.end(), [&](auto &a, auto &b){
                if (a.second != b.second) return a.second > b.second; // freq
                return a.first > b.first;                             // value
            });

            // Take top x values, sum value * freq
            long long s = 0;
            for (int t = 0; t < x; t++) {
                s += 1LL * items[t].first * items[t].second;
            }
            ans.push_back((int)s);
        }

        return ans;
    }
};