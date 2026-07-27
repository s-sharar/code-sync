class Trie {
    struct Node {
        bool end = false;
        Node* child[26] = {};
    };

    Node* root;

public:
    Trie() {
        root = new Node();
    }
    
    void insert(string word) {
        Node* cur = root;

        for (char c : word) {
            int i = c - 'a';
            if (!cur->child[i]) {
                cur->child[i] = new Node();
            }
            cur = cur->child[i];
        }

        cur->end = true;
    }
    
    bool search(string word) {
        Node* cur = root;

        for (char c : word) {
            int i = c - 'a';
            if (!cur->child[i]) return false;
            cur = cur->child[i];
        }

        return cur->end;
    }
    
    bool startsWith(string prefix) {
        Node* cur = root;

        for (char c : prefix) {
            int i = c - 'a';
            if (!cur->child[i]) return false;
            cur = cur->child[i];
        }

        return true;
    }
};