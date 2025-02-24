class Solution {
public:
    bool isAnagram(string s, string t) {

      //  string s , t ; cin >> s >> t ;
        sort (s.begin() , s.end()) ;
        sort(t.begin() , t.end()) ;

        if (s == t ) return true ;
        else return false ;
       
    }
};