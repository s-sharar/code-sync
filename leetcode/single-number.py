class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> tmp(n);
        mergeSort(nums, tmp, 0, n - 1);
        return nums;
    }

private:
    void mergeSort(vector<int>& a, vector<int>& tmp, int l, int r) {
        if (l >= r) return;
        int m = l + (r - l) / 2;
        mergeSort(a, tmp, l, m);
        mergeSort(a, tmp, m + 1, r);
        mergeHalves(a, tmp, l, m, r);
    }

    void mergeHalves(vector<int>& a, vector<int>& tmp, int l, int m, int r) {
        int i = l;       // pointer in left half [l..m]
        int j = m + 1;   // pointer in right half [m+1..r]
        int k = l;       // pointer in tmp

        while (i <= m && j <= r) {
            // <= keeps it stable: if equal, take from left half first
            if (a[i] <= a[j]) tmp[k++] = a[i++];
            else              tmp[k++] = a[j++];
        }
        while (i <= m) tmp[k++] = a[i++];
        while (j <= r) tmp[k++] = a[j++];

        for (int p = l; p <= r; p++) a[p] = tmp[p];
    }
};