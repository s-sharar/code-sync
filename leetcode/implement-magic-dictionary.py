class MagicDictionary {
    unordered_map<string, unordered_set<string>> mp; // pattern -> words that produce it

public:
    MagicDictionary() {}

    void buildDict(vector<string> dictionary) {
        mp.clear();
        for (const string& w : dictionary) {
            string p = w;
            for (int i = 0; i < (int)w.size(); i++) {
                p[i] = '*';
                mp[p].insert(w);
                p[i] = w[i];
            }
        }
    }

    bool search(string s) {
        string p = s;
        for (int i = 0; i < (int)s.size(); i++) {
            p[i] = '*';

            auto it = mp.find(p);
            if (it != mp.end()) {
                const auto& bucket = it->second;
                // need a word different from s (exactly one change)
                if (bucket.size() >= 2) return true;
                if (bucket.size() == 1 && *bucket.begin() != s) return true;
            }

            p[i] = s[i];
        }
        return false;
    }
};