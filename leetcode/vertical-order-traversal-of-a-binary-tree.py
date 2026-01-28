class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<tuple<int,int,int>> nodes; // (col, row, val)

        // DFS to collect coordinates
        function<void(TreeNode*, int, int)> dfs = [&](TreeNode* node, int row, int col) {
            if (!node) return;
            nodes.emplace_back(col, row, node->val);
            dfs(node->left,  row + 1, col - 1);
            dfs(node->right, row + 1, col + 1);
        };

        dfs(root, 0, 0);

        sort(nodes.begin(), nodes.end(), [](auto& a, auto& b) {
            auto [c1, r1, v1] = a;
            auto [c2, r2, v2] = b;
            if (c1 != c2) return c1 < c2;   // col
            if (r1 != r2) return r1 < r2;   // row
            return v1 < v2;                 // val tie-break
        });

        vector<vector<int>> ans;
        int i = 0;
        while (i < (int)nodes.size()) {
            int col = get<0>(nodes[i]);
            vector<int> group;
            while (i < (int)nodes.size() && get<0>(nodes[i]) == col) {
                group.push_back(get<2>(nodes[i])); // val
                i++;
            }
            ans.push_back(std::move(group));
        }
        return ans;
    }
};