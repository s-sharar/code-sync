class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int l = 0, r = (int)nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mid % 2 == 1) mid--;          // make mid even
            if (nums[mid] == nums[mid + 1])   // pair is intact
                l = mid + 2;
            else
                r = mid;
        }
        return nums[l];
    }
};