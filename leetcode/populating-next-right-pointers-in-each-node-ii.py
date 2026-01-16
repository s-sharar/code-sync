class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        queue<Node*> q;
        q.push(root);

        while (!q.empty()) {
            int sz = q.size();
            Node* prev = nullptr;

            for (int i = 0; i < sz; ++i) {
                Node* cur = q.front(); q.pop();
                if (prev) prev->next = cur;
                prev = cur;

                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
            }
            prev->next = nullptr;
        }
        return root;
    }
};