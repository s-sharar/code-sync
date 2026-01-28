class Solution {
    Node* dfs(Node* head) {
        Node* curr = head;
        Node* tail = head;

        while (curr) {
            Node* next = curr->next;

            if (curr->child) {
                Node* childHead = curr->child;
                Node* childTail = dfs(childHead);

                // splice child between curr and next
                curr->child = nullptr;
                curr->next = childHead;
                childHead->prev = curr;

                if (next) {
                    childTail->next = next;
                    next->prev = childTail;
                }

                tail = childTail;
                curr = childTail; // continue from end of spliced child list
            } else {
                tail = curr;
            }

            curr = curr->next;
        }

        return tail;
    }

public:
    Node* flatten(Node* head) {
        if (!head) return nullptr;
        dfs(head);
        head->prev = nullptr;
        return head;
    }
};