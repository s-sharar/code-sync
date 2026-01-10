class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> prefixes;
        for (int elem : arr2) {
            while (elem > 0) {
                prefixes.insert(elem);
                elem /= 10;
            }
        }
        int maxPref = INT_MIN;
        for (int elem : arr1) {
            int cand = INT_MIN;
            while (elem > 0) {
                if (prefixes.count(elem)) {
                    cand = elem;
                    break;
                }
                elem /= 10;
            }
            maxPref = max(maxPref, cand);
        }
        if (maxPref == INT_MIN) return 0;
        int len = 0;
        while (maxPref) {
            ++len;
            maxPref /= 10;
        }
        return len;
    }
};