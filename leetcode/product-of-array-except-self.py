class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> res(n, 1);

        // prefix products into res
        int pref = 1;
        for (int i = 0; i < n; i++) {
            res[i] = pref;
            pref *= nums[i];
        }

        // multiply by suffix products
        int suff = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= suff;
            suff *= nums[i];
        }

        return res;
    }
};