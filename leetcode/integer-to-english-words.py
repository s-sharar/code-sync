class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero";

        vector<string> below10 = {"", "One","Two","Three","Four","Five","Six","Seven","Eight","Nine"};
        vector<string> below20 = {"Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"};
        vector<string> tens = {"", "", "Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"};

        auto under100 = [&](int x) -> string {
            string s;
            if (x >= 20) {
                s += tens[x / 10];
                if (x % 10) s += " " + below10[x % 10];
            } else if (x >= 10) {
                s += below20[x - 10];
            } else if (x > 0) {
                s += below10[x];
            }
            return s;
        };

        function<string(int)> under1000 = [&](int x) -> string {
            string s;
            if (x >= 100) {
                s += below10[x / 100] + " Hundred";
                if (x % 100) s += " " + under100(x % 100);
            } else {
                s += under100(x);
            }
            return s;
        };

        auto addChunk = [&](string& res, int chunk, const string& label) {
            if (chunk == 0) return;
            if (!res.empty()) res += " ";
            res += under1000(chunk);
            if (!label.empty()) res += " " + label;
        };

        string res;
        addChunk(res, num / 1000000000, "Billion");
        addChunk(res, (num / 1000000) % 1000, "Million");
        addChunk(res, (num / 1000) % 1000, "Thousand");
        addChunk(res, num % 1000, "");

        return res;
    }
};