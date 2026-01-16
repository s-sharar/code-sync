/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        Node* cur = root;                 // head of current level
        while (cur) {
            Node dummy(0);
            Node* tail = &dummy;          // build next level list

            for (Node* p = cur; p; p = p->next) {
                if (p->left)  { tail->next = p->left;  tail = tail->next; }
                if (p->right) { tail->next = p->right; tail = tail->next; }
            }

            cur = dummy.next;             // move down a level
        }
        return root;
    }
};