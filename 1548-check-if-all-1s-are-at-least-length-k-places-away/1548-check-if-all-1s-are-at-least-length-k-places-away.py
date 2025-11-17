class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = None
        i = 0
        while(i < len(nums) and nums[i] != 1 ):
            i += 1
        
        last_one = i
        i += 1

        while(i < len(nums)):

            if(nums[i] == 1):
                
                if(i - last_one - 1 < k):
                    return False
                
                last_one = i

            i += 1
        
        return True