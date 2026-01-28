#include <bits/stdc++.h>
using namespace std;

class UndergroundSystem {
    struct CheckInInfo {
        string station;
        int time;
    };
    struct Agg {
        long long sum = 0;
        int cnt = 0;
    };

    unordered_map<int, CheckInInfo> checkins;
    unordered_map<string, Agg> stats;

    static string key(const string& a, const string& b) {
        // delimiter unlikely to appear in station names
        return a + "#" + b;
    }

public:
    UndergroundSystem() {}

    void checkIn(int id, string stationName, int t) {
        checkins[id] = {stationName, t};
    }

    void checkOut(int id, string stationName, int t) {
        auto it = checkins.find(id);
        // per problem constraints, this should always exist
        const string& start = it->second.station;
        int startTime = it->second.time;

        int duration = t - startTime;
        auto& ag = stats[key(start, stationName)];
        ag.sum += duration;
        ag.cnt += 1;

        checkins.erase(it);
    }

    double getAverageTime(string startStation, string endStation) {
        auto& ag = stats[key(startStation, endStation)];
        return (double)ag.sum / ag.cnt;
    }
};