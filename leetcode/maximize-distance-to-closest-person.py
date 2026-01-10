class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int person1 = -1;
        int i = 0;
        int maxDist = -1;
        int initialPerson1 = -1;
        while (person1 == -1) {
            if (seats[i] != 0) person1 = i;
            i++;
        }
        initialPerson1 = person1;
        for (; i < seats.size(); ++i) {
            if (seats[i] != 0) {
                maxDist = max(maxDist, i - person1);
                person1 = i;
            }
        }
        if (maxDist == -1) {
            return max(person1, int(seats.size() - person1 - 1));
        }
        return max(initialPerson1, max(maxDist / 2, (int)seats.size() - person1 - 1));
    }
};