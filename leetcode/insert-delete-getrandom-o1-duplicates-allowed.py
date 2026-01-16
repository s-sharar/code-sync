class RandomizedCollection {
    vector<int> a;
    unordered_map<int, unordered_set<int>> pos;

public:
    bool insert(int val) {
        bool notPresent = (pos.find(val) == pos.end() || pos[val].empty());
        a.push_back(val);
        pos[val].insert((int)a.size() - 1);
        return notPresent;
    }

    bool remove(int val) {
        auto it = pos.find(val);
        if (it == pos.end() || it->second.empty()) return false;

        int i = *it->second.begin();      // index of one occurrence of val
        int j = (int)a.size() - 1;        // last index
        int last = a[j];

        // erase i from val's set
        it->second.erase(i);

        if (i != j) {
            // move last into position i
            a[i] = last;

            // update last's indices set: j -> i
            pos[last].erase(j);
            pos[last].insert(i);
        }

        a.pop_back();
        if (it->second.empty()) pos.erase(it);
        return true;
    }

    int getRandom() {
        return a[rand() % a.size()];
    }
};