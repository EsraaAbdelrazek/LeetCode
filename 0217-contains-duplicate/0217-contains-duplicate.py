class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
        # count = Counter (nums) 
        # for  i in nums : 
        #     if count [i] > 1 : 
        #         return True 
        
        # return False 
