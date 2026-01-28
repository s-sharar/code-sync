class OrderedStream {
    vector<string> data;
    vector<char> filled;
    int ptr;

public:
    OrderedStream(int n) : data(n + 1), filled(n + 1, 0), ptr(1) {}

    vector<string> insert(int idKey, string value) {
        data[idKey] = value;
        filled[idKey] = 1;

        vector<string> out;
        while (ptr < (int)data.size() && filled[ptr]) {
            out.push_back(data[ptr]);
            ptr++;
        }
        return out;
    }
};