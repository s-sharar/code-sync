class Allocator {
public:
    vector<int> mem;

    Allocator(int n) {
        mem.assign(n, 0); // 0 means free
    }
    
    int allocate(int size, int mID) {
        int n = mem.size();

        for (int i = 0; i < n; i++) {
            if (mem[i] != 0) continue;

            int j = i;
            while (j < n && mem[j] == 0 && j - i < size) {
                j++;
            }

            if (j - i == size) {
                for (int k = i; k < j; k++) {
                    mem[k] = mID;
                }
                return i;
            }

            i = j; // skip checked block
        }

        return -1;
    }
    
    int freeMemory(int mID) {
        int freed = 0;

        for (int i = 0; i < mem.size(); i++) {
            if (mem[i] == mID) {
                mem[i] = 0;
                freed++;
            }
        }

        return freed;
    }
};
/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator* obj = new Allocator(n);
 * int param_1 = obj->allocate(size,mID);
 * int param_2 = obj->freeMemory(mID);
 */