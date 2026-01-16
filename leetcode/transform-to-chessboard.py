class Solution {
public:
    int movesToChessboard(vector<vector<int>>& board) {
        int n = board.size();

        // 1) 2x2 XOR validity check
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ( (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0 )
                    return -1;
            }
        }

        // counts of 1s in first row / first col
        int rowSum = 0, colSum = 0;
        for (int i = 0; i < n; i++) {
            rowSum += board[0][i];
            colSum += board[i][0];
        }

        // must be balanced appropriately
        auto okCount = [&](int s) {
            if (n % 2 == 0) return s == n/2;
            return s == n/2 || s == n/2 + 1;
        };
        if (!okCount(rowSum) || !okCount(colSum)) return -1;

        // 3) mismatches for rows / cols for both possible starting bits
        int rowMismatch0 = 0, rowMismatch1 = 0;
        int colMismatch0 = 0, colMismatch1 = 0;

        for (int i = 0; i < n; i++) {
            // first column should be i%2 (start=0) or 1-i%2 (start=1)
            if (board[i][0] != (i % 2)) rowMismatch0++;
            if (board[i][0] != (1 - (i % 2))) rowMismatch1++;

            // first row similarly
            if (board[0][i] != (i % 2)) colMismatch0++;
            if (board[0][i] != (1 - (i % 2))) colMismatch1++;
        }

        auto movesFromMismatch = [&](int mismatch0, int mismatch1, int onesCount) {
            if (n % 2 == 0) {
                return min(mismatch0, mismatch1) / 2;
            } else {
                // start is forced: if ones are more, pattern must start with 1; else start with 0
                // For start=0, expected ones count is n/2; for start=1, expected ones count is n/2+1
                if (onesCount == n/2) return mismatch0 / 2;      // start with 0
                else return mismatch1 / 2;                       // start with 1
            }
        };

        int rowMoves = movesFromMismatch(rowMismatch0, rowMismatch1, colSum);
        int colMoves = movesFromMismatch(colMismatch0, colMismatch1, rowSum);

        return rowMoves + colMoves;
    }
};