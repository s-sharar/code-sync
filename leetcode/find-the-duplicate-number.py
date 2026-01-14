class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];

        // Phase 1: find intersection point inside the cycle
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Phase 2: find entrance to the cycle (the duplicate)
        int ptr = nums[0];
        while (ptr != slow) {
            ptr = nums[ptr];
            slow = nums[slow];
        }
        return ptr;
    }
};