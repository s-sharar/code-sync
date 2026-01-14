#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */

class Codec {
    void ser(TreeNode* root, string& out) {
        if (!root) {
            out += "#,";
            return;
        }
        out += to_string(root->val);
        out += ",";
        ser(root->left, out);
        ser(root->right, out);
    }

    TreeNode* deser(vector<string>& tok, int& i) {
        if (tok[i] == "#") {
            ++i;
            return nullptr;
        }
        TreeNode* node = new TreeNode(stoi(tok[i]));
        ++i;
        node->left = deser(tok, i);
        node->right = deser(tok, i);
        return node;
    }

public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string out;
        ser(root, out);
        return out;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<string> tok;
        string cur;
        for (char c : data) {
            if (c == ',') {
                tok.push_back(cur);
                cur.clear();
            } else {
                cur.push_back(c);
            }
        }
        // (serialize always ends with a comma, so cur should be empty here)

        int i = 0;
        return tok.empty() ? nullptr : deser(tok, i);
    }
};