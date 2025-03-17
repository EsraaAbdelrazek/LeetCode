class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:

        num1 = [nums[0]]
        num2 = [nums[1]]

        for i in range (2 , len (nums)) : 
            if num1[-1] > num2[-1] : 
                num1.append (nums[i])
            else : 
                 num2.append (nums[i])

        return num1 +num2 