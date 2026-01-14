class Solution {
    struct Node {
        Node* child[26];
        vector<string> top; // up to 3 lexicographically smallest products for this prefix
        Node() {
            memset(child, 0, sizeof(child));
        }
    };

    void insert(Node* root, const string& s) {
        Node* cur = root;
        for (char c : s) {
            int i = c - 'a';
            if (!cur->child[i]) cur->child[i] = new Node();
            cur = cur->child[i];
            if ((int)cur->top.size() < 3) cur->top.push_back(s);
        }
    }

public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());

        Node* root = new Node();
        for (auto &p : products) insert(root, p);

        vector<vector<string>> res;
        Node* cur = root;

        for (char c : searchWord) {
            if (!cur) {
                res.push_back({});
                continue;
            }
            int i = c - 'a';
            cur = cur->child[i];
            if (!cur) res.push_back({});
            else res.push_back(cur->top);
        }
        return res;
    }
};