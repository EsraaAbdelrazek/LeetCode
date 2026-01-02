class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        st = set () 
       
        for i in nums : 
            if i not in st : 
                st.add(i) 

            else : return i  
        