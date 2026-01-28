class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        std::vector<ListNode*> v;
        for (ListNode* cur = head; cur; cur = cur->next) v.push_back(cur);

        int l = 0, r = (int)v.size() - 1;
        ListNode* cur = nullptr;

        while (l <= r) {
            if (!cur) {               // first node
                cur = v[l++];
            } else {
                cur->next = v[l++];
                cur = cur->next;
            }
            if (l > r) break;

            cur->next = v[r--];
            cur = cur->next;
        }

        cur->next = nullptr; // IMPORTANT: terminate
    }
};