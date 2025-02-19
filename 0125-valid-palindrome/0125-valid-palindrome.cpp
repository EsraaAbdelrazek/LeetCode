class Solution {
public:
    bool isPalindrome(string s) {
        string str = "" ; 
        for (int i =0 ; i< s.size() ; i++){
		if( (s[i] >='a' && s[i] <='z') || (s[i] >='0' && s[i] <='9') ){
			str += s[i] ; 
		}else if (s[i] >='A' && s[i] <='Z'){
			s[i] += 32 ; 
			str += (char) s[i] ; 
		}
		
	}int i =0 , j = str.size()-1 ; 
	bool flag = true ; 
	
	while (i<=j){
		if (str[i] != str[j]){
			flag = false ; 
			break ; 
		}else {
			i++ ; 
			j-- ; 
		}
	}
    if(flag) return true ; 
    else return false ; 
    }
};