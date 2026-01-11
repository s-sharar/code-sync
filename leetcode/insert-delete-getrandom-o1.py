class RandomizedSet {
    vector<int> vals;
    unordered_map<int, int> idx; // val -> index in vals
public:
    RandomizedSet() {
        vals.clear();
        idx.clear();
    }

    bool insert(int val) {
        if (idx.count(val)) return false;
        idx[val] = (int)vals.size();
        vals.push_back(val);
        return true;
    }

    bool remove(int val) {
        auto it = idx.find(val);
        if (it == idx.end()) return false;

        int removeIndex = it->second;
        int lastVal = vals.back();
        int lastIndex = (int)vals.size() - 1;

        // move lastVal into removeIndex (unless it's already last)
        vals[removeIndex] = lastVal;
        idx[lastVal] = removeIndex;

        vals.pop_back();
        idx.erase(it);
        return true;
    }

    int getRandom() {
        int r = rand() % vals.size();
        return vals[r];
    }
};