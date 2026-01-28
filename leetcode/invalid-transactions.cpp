#include <bits/stdc++.h>
using namespace std;

struct Tx {
    string name, city, original;
    int time, amount;
};

static vector<string> split4(const string& s) {
    vector<string> parts;
    parts.reserve(4);
    string cur;
    for (char c : s) {
        if (c == ',') { parts.push_back(cur); cur.clear(); }
        else cur.push_back(c);
    }
    parts.push_back(cur);
    return parts; // size 4
}

class Solution {
public:
    vector<string> invalidTransactions(vector<string>& transactions) {
        int n = (int)transactions.size();
        vector<Tx> tx(n);

        for (int i = 0; i < n; i++) {
            auto p = split4(transactions[i]);
            tx[i].name = p[0];
            tx[i].time = stoi(p[1]);
            tx[i].amount = stoi(p[2]);
            tx[i].city = p[3];
            tx[i].original = transactions[i];
        }

        vector<int> ord(n);
        iota(ord.begin(), ord.end(), 0);
        sort(ord.begin(), ord.end(), [&](int a, int b) {
            if (tx[a].name != tx[b].name) return tx[a].name < tx[b].name;
            return tx[a].time < tx[b].time;
        });

        vector<bool> bad(n, false);

        // Rule 1: amount > 1000
        for (int i = 0; i < n; i++) {
            if (tx[i].amount > 1000) bad[i] = true;
        }

        // Rule 2: same name, different city, within 60 minutes
        int i = 0;
        while (i < n) {
            int j = i;
            string name = tx[ord[i]].name;
            while (j < n && tx[ord[j]].name == name) j++;

            // Process ord[i..j-1] (same name, sorted by time)
            for (int r = i; r < j; r++) {
                int idxR = ord[r];
                // scan backward while within 60 minutes
                for (int l = r - 1; l >= i; l--) {
                    int idxL = ord[l];
                    if (tx[idxR].time - tx[idxL].time > 60) break;
                    if (tx[idxR].city != tx[idxL].city) {
                        bad[idxR] = true;
                        bad[idxL] = true;
                    }
                }
            }

            i = j;
        }

        vector<string> res;
        for (int k = 0; k < n; k++) {
            if (bad[k]) res.push_back(tx[k].original);
        }
        return res;
    }
};