class Spreadsheet {
    vector<vector<int>> grid;

    int getOperand(string s) {
        // Number
        if (isdigit(s[0])) return stoi(s);

        // Cell reference
        int col = s[0] - 'A';
        int row = stoi(s.substr(1)) - 1;
        return grid[row][col];
    }

public:
    Spreadsheet(int rows) {
        grid.assign(rows, vector<int>(26, 0));
    }

    void setCell(string cell, int value) {
        int col = cell[0] - 'A';
        int row = stoi(cell.substr(1)) - 1;

        grid[row][col] = value;
    }

    void resetCell(string cell) {
        int col = cell[0] - 'A';
        int row = stoi(cell.substr(1)) - 1;

        grid[row][col] = 0;
    }

    int getValue(string formula) {
        // Remove '='
        formula = formula.substr(1);

        int plus = formula.find('+');

        string left = formula.substr(0, plus);
        string right = formula.substr(plus + 1);

        return getOperand(left) + getOperand(right);
    }
};