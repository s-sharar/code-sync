class Solution {
public:
    int minSteps(string s, string t) {
        int cnt[26] = {0};

        for (char c : s) cnt[c - 'a']++;
        for (char c : t) cnt[c - 'a']--;

        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] > 0) ans += cnt[i];
        }
        return ans;
    }
};