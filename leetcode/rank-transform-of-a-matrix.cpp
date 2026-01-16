#include <bits/stdc++.h>
using namespace std;

class Solution {
    struct DSU {
        vector<int> p, r;
        DSU(int n=0){ init(n); }
        void init(int n){
            p.resize(n);
            r.assign(n,0);
            iota(p.begin(), p.end(), 0);
        }
        int find(int x){ return p[x]==x? x : p[x]=find(p[x]); }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(r[a]<r[b]) swap(a,b);
            p[b]=a;
            if(r[a]==r[b]) r[a]++;
        }
    };

public:
    vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
        int R = (int)matrix.size(), C = (int)matrix[0].size();

        // value -> list of cells (r,c)
        map<int, vector<pair<int,int>>> groups;
        groups.clear();
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                groups[matrix[i][j]].push_back({i,j});
            }
        }

        vector<int> rowMax(R, 0), colMax(C, 0);
        vector<vector<int>> ans(R, vector<int>(C, 0));

        for (auto &entry : groups) {
            auto &cells = entry.second;
            int k = (int)cells.size();

            // DSU indices 0..k-1 represent cells in this value group
            DSU dsu(k);

            // To union quickly: for this value, remember first seen cell index in each row/col
            unordered_map<int,int> firstInRow;
            unordered_map<int,int> firstInCol;
            firstInRow.reserve(k*2);
            firstInCol.reserve(k*2);

            for (int idx = 0; idx < k; idx++) {
                int r = cells[idx].first;
                int c = cells[idx].second;

                auto itR = firstInRow.find(r);
                if (itR != firstInRow.end()) dsu.unite(idx, itR->second);
                else firstInRow[r] = idx;

                auto itC = firstInCol.find(c);
                if (itC != firstInCol.end()) dsu.unite(idx, itC->second);
                else firstInCol[c] = idx;
            }

            // For each component root, compute needed rank = 1 + max(rowMax[r], colMax[c]) over members
            unordered_map<int,int> compBase; // root -> base max
            compBase.reserve(k*2);

            for (int idx = 0; idx < k; idx++) {
                int root = dsu.find(idx);
                int r = cells[idx].first;
                int c = cells[idx].second;
                int base = max(rowMax[r], colMax[c]);
                auto it = compBase.find(root);
                if (it == compBase.end()) compBase[root] = base;
                else it->second = max(it->second, base);
            }

            // Assign ranks to cells in this group based on their component
            vector<int> newRank(k);
            for (int idx = 0; idx < k; idx++) {
                int root = dsu.find(idx);
                newRank[idx] = compBase[root] + 1;
                ans[cells[idx].first][cells[idx].second] = newRank[idx];
            }

            // After all ranks for this value are decided, update rowMax/colMax
            for (int idx = 0; idx < k; idx++) {
                int r = cells[idx].first;
                int c = cells[idx].second;
                rowMax[r] = max(rowMax[r], newRank[idx]);
                colMax[c] = max(colMax[c], newRank[idx]);
            }
        }

        return ans;
    }
};