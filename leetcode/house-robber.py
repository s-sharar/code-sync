class Solution {
public:
    int rob(vector<int>& nums) {
        int curr = 0, prev = 0;
        for (int x : nums) {
            int temp = curr;
            curr = max(curr, prev + x);
            prev = temp;
        }
        return curr;
    }
};