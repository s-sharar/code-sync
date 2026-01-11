class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> st(nums.begin(), nums.end());
        int curr = 0;
        int last = INT_MIN;
        int maxSeq = 0;
        for (int elem : st) {
            if (last == INT_MIN || elem == last + 1) {
                curr++;
                maxSeq = max(maxSeq, curr);
                last = elem;
            } else {
                curr = 1;
                last = elem;
            }
        }
        return maxSeq;
    }
};