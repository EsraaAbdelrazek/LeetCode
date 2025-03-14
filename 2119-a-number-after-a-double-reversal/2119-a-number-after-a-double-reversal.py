class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
              return str(num) == str(int(str(num)[::-1]))[::-1]
        # num_str = str (num)
        # if num_str [-1] == '0' and len (num_str) == 1 : 
        #     return True 

        # if num_str [-1] == '0' and len (num_str) != 1 : 
        #     return False 
        # reversed1 = num_str[::-1] 
        # reversed2 = reversed1 [::-1] 

        # if reversed2 == num_str : 
        #         return True 
        # else : 
        #         return False 

        