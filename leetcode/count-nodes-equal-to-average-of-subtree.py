/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int ret = 0;
    pair<int, int> dfs(TreeNode* r) {
        if (!r) return {0, 0};
        auto pLeft = dfs(r->left);
        auto pRight = dfs(r->right);
        int total = pLeft.first + pRight.first + r->val;
        int count = pLeft.second + pRight.second + 1;
        if (r->val == (total / count)) ret++;
        return {total, count};
    }
public:
    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return ret;
    }
};