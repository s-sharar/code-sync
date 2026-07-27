class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) {
            return a->val > b->val; // min-heap
        };

        priority_queue<
            ListNode*,
            vector<ListNode*>,
            decltype(cmp)
        > pq(cmp);

        // Initially add the head of every non-empty list
        for (ListNode* head : lists) {
            if (head) pq.push(head);
        }

        ListNode dummy;
        ListNode* tail = &dummy;

        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();

            tail->next = node;
            tail = tail->next;

            // Incrementally expose the next node from this list
            if (node->next) {
                pq.push(node->next);
            }
        }

        return dummy.next;
    }
};