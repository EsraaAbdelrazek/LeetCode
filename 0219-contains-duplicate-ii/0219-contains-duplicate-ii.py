class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = defaultdict()
        for i , v in enumerate (nums) : 
            if v in index_dict and (i - index_dict[v] )<= k : 
                return True 
            index_dict[v] = i
        return False    
            # Time Limit
        # for val , inx in index_dict.items () : 
        #     for i in range (len  (inx)) : 
        #         for j in range (i +1 , len (inx)) : 
        #                if abs(inx[i] - inx[j]) <= k:
        #                 return True

        # for i in range (len (nums)) : 
        #      index_dict[nums[i]] .append (i)



        