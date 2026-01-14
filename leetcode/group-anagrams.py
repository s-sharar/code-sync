class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;

        for (const string& s : strs) {
            int cnt[26] = {0};
            for (char c : s) cnt[c - 'a']++;

            // build a unique key from counts: "#1#0#0...#2"
            string key;
            key.reserve(26 * 3);
            for (int i = 0; i < 26; ++i) {
                key.push_back('#');
                key += to_string(cnt[i]);
            }

            mp[key].push_back(s);
        }

        vector<vector<string>> res;
        res.reserve(mp.size());
        for (auto& [k, group] : mp) res.push_back(std::move(group));
        return res;
    }
};