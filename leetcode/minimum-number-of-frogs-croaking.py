class Solution {
    unordered_map<char, int> count;
    bool valid() {
        return count['r'] <= count['c'] && count['o'] <= count['r'] &&
            count['a'] <= count['o'] && count['k'] <= count['a'];
    }
    bool validAtEnd() {
        return count['r'] == count['c'] && count['o'] == count['r'] &&
            count['a'] == count['o'] && count['k'] == count['a'];
    }
public:
    int minNumberOfFrogs(string croakOfFrogs) {
        int maxCount = 0;
        int currCount = 0;
        for (char c : croakOfFrogs) {
            count[c]++;
            if (!valid()) return -1;
            if (c == 'c') {
                ++currCount;
                maxCount = max(maxCount, currCount);
            }
            if (c == 'k') {
                --currCount;
            }
        }
        if (!validAtEnd()) return -1;
        return maxCount;
    }
};