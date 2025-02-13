class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size() ; 
       // for (int i =0 ; i < n  ;i++) cin >> arr[i] ; 
        string str = "" ; 
        for (int i = 0 ; i< strs[0].size() ; i++){
        char c = strs[0][i] ; 
		bool b = true ; 
		for(int j= 1 ; j < n ; j++){
			if(c != strs[j][i]) b = false  ;
		}
		if (b)		str += c ; 
		else break ; 
    
	} 
    return str ; 
    }
};
/*
	int n; cin >> n ; 
	string arr [n] ; 
	string str = "" ; 
	for (int i =0 ; i < n  ;i++) cin >> arr[i] ; 
	
	for (int i = 0 ; i< arr[0].size() ; i++){
		char c = arr[0][i] ; 
		bool b = true ; 
		for(int j= 1 ; j < n ; j++){
			if(c != arr[j][i]) b = false  ;
		}
		if (b)		str += c ; 
		else break ; 
	
	} 
	cout << str ; 
*/