class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord)) return 0;

        int L = beginWord.size();

        // pattern -> list of words having that pattern
        unordered_map<string, vector<string>> bucket;
        bucket.reserve(wordList.size() * L * 2);

        for (const string& w : wordList) {
            for (int i = 0; i < L; i++) {
                string p = w;
                p[i] = '*';
                bucket[p].push_back(w);
            }
        }

        queue<pair<string,int>> q;
        unordered_set<string> vis;
        vis.reserve(dict.size() * 2);

        q.push({beginWord, 1});
        vis.insert(beginWord);

        while (!q.empty()) {
            auto [w, dist] = q.front(); q.pop();
            if (w == endWord) return dist;

            for (int i = 0; i < L; i++) {
                string p = w;
                p[i] = '*';

                auto it = bucket.find(p);
                if (it == bucket.end()) continue;

                for (const string& nxt : it->second) {
                    if (!vis.count(nxt)) {
                        vis.insert(nxt);
                        q.push({nxt, dist + 1});
                    }
                }
                // important: don't expand this pattern again
                it->second.clear();
            }
        }

        return 0;
    }

};