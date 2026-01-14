class DSU {
    vector<int> p, sz;
public:
    DSU(int n): p(n), sz(n,1) { iota(p.begin(), p.end(), 0); }
    int find(int x){ return p[x]==x ? x : p[x]=find(p[x]); }
    void unite(int a,int b){
        a=find(a); b=find(b);
        if(a==b) return;
        if(sz[a]<sz[b]) swap(a,b);
        p[b]=a; sz[a]+=sz[b];
    }
    int size(int x){ return sz[find(x)]; }
};

class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int n = row.size();
        int m = n/2;                  // number of couples
        DSU dsu(m);

        for(int i=0;i<n;i+=2){
            int c1 = row[i] / 2;
            int c2 = row[i+1] / 2;
            dsu.unite(c1, c2);
        }

        // count component sizes by root
        unordered_map<int,int> comp;
        for(int c=0;c<m;c++) comp[dsu.find(c)]++;

        int ans = 0;
        for(auto &kv: comp) ans += kv.second - 1;
        return ans;
    }
};