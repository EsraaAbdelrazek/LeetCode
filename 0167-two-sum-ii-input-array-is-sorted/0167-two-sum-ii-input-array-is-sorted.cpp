class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size() ; 
        int sum =0 ; 
        int i =0 , j = n-1 ; 
        while (i<=j){
            sum = numbers[i] + numbers[j] ; 
            if (sum > target ){
                j-- ; 
            }
            else if (sum < target){
                i++ ; 
            }
           else break ; 
        }
        return {i+1 , j+1} ; 
    }
};