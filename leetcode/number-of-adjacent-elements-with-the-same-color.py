class Solution {
public:
    vector<int> colorTheArray(int n, vector<vector<int>>& queries) {
        vector<int> res(n, 0);
        vector<int> ans;
        int same = 0;
        for (auto elem : queries) {
            int idx = elem[0], val = elem[1];
            if (idx > 0 && res[idx] != 0 && res[idx] == res[idx - 1]) --same;
            if (idx < n - 1 && res[idx] != 0 && res[idx] == res[idx + 1]) --same;
            res[idx] = val;
            if (idx > 0 && res[idx] != 0 && res[idx] == res[idx - 1]) ++same;
            if (idx < n - 1 && res[idx] != 0 && res[idx] == res[idx + 1]) ++same;
            ans.push_back(same);
        }
        return ans;
    }
};