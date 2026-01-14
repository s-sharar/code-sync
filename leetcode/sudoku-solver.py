class Solution {
    static constexpr int FULL = (1 << 9) - 1; // 9 bits for digits 1..9

    vector<int> row, col, box;               // size 9, bitmasks
    vector<pair<int,int>> empties;

    int boxId(int r, int c) { return (r/3)*3 + (c/3); }

    bool dfs(vector<vector<char>>& board) {
        int bestR = -1, bestC = -1;
        int bestMask = 0;
        int bestCount = 10;

        // pick empty cell with minimum candidates (MRV)
        for (auto [r, c] : empties) {
            if (board[r][c] != '.') continue;

            int b = boxId(r, c);
            int used = row[r] | col[c] | box[b];
            int mask = (~used) & FULL;
            int cnt = __builtin_popcount((unsigned)mask);

            if (cnt == 0) return false;
            if (cnt < bestCount) {
                bestCount = cnt;
                bestR = r; bestC = c;
                bestMask = mask;
                if (cnt == 1) break;
            }
        }

        // no empties left
        if (bestR == -1) return true;

        int r = bestR, c = bestC;
        int b = boxId(r, c);

        // try each candidate digit
        for (int mask = bestMask; mask; mask &= (mask - 1)) {
            int bit = mask & -mask;                 // isolate lowest set bit
            int d = __builtin_ctz((unsigned)bit);   // bit index 0..8

            board[r][c] = char('1' + d);
            row[r] |= bit; col[c] |= bit; box[b] |= bit;

            if (dfs(board)) return true;

            row[r] ^= bit; col[c] ^= bit; box[b] ^= bit;
            board[r][c] = '.';
        }
        return false;
    }

public:
    void solveSudoku(vector<vector<char>>& board) {
        row.assign(9, 0);
        col.assign(9, 0);
        box.assign(9, 0);
        empties.clear();

        // build masks
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] == '.') {
                    empties.push_back({r, c});
                } else {
                    int d = board[r][c] - '1';   // 0..8
                    int bit = 1 << d;
                    int b = boxId(r, c);
                    row[r] |= bit;
                    col[c] |= bit;
                    box[b] |= bit;
                }
            }
        }

        dfs(board);
    }
};