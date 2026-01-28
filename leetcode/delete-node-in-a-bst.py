class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;

        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            // found node
            if (!root->left && !root->right) {
                return nullptr;
            }
            if (!root->left) return root->right;
            if (!root->right) return root->left;

            // two children: use successor (min in right subtree)
            TreeNode* succ = root->right;
            while (succ->left) succ = succ->left;

            root->val = succ->val;                 // copy value
            root->right = deleteNode(root->right, succ->val); // delete successor
        }
        return root;
    }
};