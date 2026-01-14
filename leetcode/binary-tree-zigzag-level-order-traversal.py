class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};

        vector<vector<int>> res;
        queue<TreeNode*> q;
        q.push(root);

        bool leftToRight = true;

        while (!q.empty()) {
            int n = (int)q.size();
            vector<int> level(n);

            for (int i = 0; i < n; ++i) {
                TreeNode* cur = q.front(); q.pop();

                int idx = leftToRight ? i : (n - 1 - i);
                level[idx] = cur->val;

                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
            }

            res.push_back(std::move(level));
            leftToRight = !leftToRight;
        }

        return res;
    }
};