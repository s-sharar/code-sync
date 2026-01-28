class Solution {
public:
    bool equalFrequency(string word) {
        int cnt[26] = {0};
        for (char c : word) cnt[c - 'a']++;

        auto ok = [&]() -> bool {
            int target = 0;
            for (int j = 0; j < 26; j++) {
                if (cnt[j] == 0) continue;
                if (target == 0) target = cnt[j];
                else if (cnt[j] != target) return false;
            }
            return true; // 0/1 non-zero freqs also return true
        };

        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 0) continue;
            cnt[i]--;
            if (ok()) return true;
            cnt[i]++;
        }
        return false;
    }
};