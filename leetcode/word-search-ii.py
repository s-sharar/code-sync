class Solution {
    struct Node {
        int next[26];
        string word; // non-empty if a word ends here
        Node() : word("") { fill(begin(next), end(next), -1); }
    };

    vector<Node> trie;

    int addNode() {
        trie.emplace_back();
        return (int)trie.size() - 1;
    }

    void insert(const string& w) {
        int cur = 0;
        for (char ch : w) {
            int c = ch - 'a';
            if (trie[cur].next[c] == -1) trie[cur].next[c] = addNode();
            cur = trie[cur].next[c];
        }
        trie[cur].word = w;
    }

    int m, n;
    vector<string> ans;

    void dfs(vector<vector<char>>& board, int i, int j, int node) {
        char ch = board[i][j];
        if (ch == '#') return;

        int c = ch - 'a';
        int nxt = trie[node].next[c];
        if (nxt == -1) return;

        // consume this char
        board[i][j] = '#';

        if (!trie[nxt].word.empty()) {
            ans.push_back(trie[nxt].word);
            trie[nxt].word.clear(); // avoid duplicates
        }

        if (i > 0) dfs(board, i - 1, j, nxt);
        if (i + 1 < m) dfs(board, i + 1, j, nxt);
        if (j > 0) dfs(board, i, j - 1, nxt);
        if (j + 1 < n) dfs(board, i, j + 1, nxt);

        board[i][j] = ch; // unvisit
    }

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        m = (int)board.size();
        n = (int)board[0].size();

        trie.clear();
        trie.reserve(1 + 10 * words.size());
        addNode(); // root at 0

        for (auto& w : words) insert(w);

        ans.clear();
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                dfs(board, i, j, 0);

        return ans;
    }
};