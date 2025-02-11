class Solution {
public:
    string removeOccurrences(string s, string part) {
        size_t pos;
        while ((pos = s.find(part)) !=
               string::npos) {           // Find the first occurrence
            s.erase(pos, part.length()); // Remove `part`
        }
        return s;
    }
};
