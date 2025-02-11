class Solution:
    def removeDuplicates(self, nums):
        if not nums : 
         return 0 

        unq_inx = 0 

        for i in range (1 , len (nums)) : 
            if nums [ unq_inx ] != nums[i] : 
                unq_inx += 1 
                nums [unq_inx ] = nums[i]



        return unq_inx +1 