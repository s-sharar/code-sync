class Solution {
public:
    int ans = INT_MIN;

    int dfs(TreeNode* node) {
        if (!node) return 0;

        int left = max(0, dfs(node->left));
        int right = max(0, dfs(node->right));

        // path that peaks at node (can use both sides)
        ans = max(ans, node->val + left + right);

        // path going up to parent (must choose one side)
        return node->val + max(left, right);
    }

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans;
    }
};