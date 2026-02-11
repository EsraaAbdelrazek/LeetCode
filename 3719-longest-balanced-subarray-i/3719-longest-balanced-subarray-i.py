class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0

        i = 0
        while(i < len(nums)):

            even = set()
            odd = set()
            j = i
            while(j < len(nums)):
                
                if(nums[j] % 2 == 0):
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if(len(even) == len(odd) and (j - i + 1) > ans):
                    ans = j - i + 1
                

                j += 1
            i += 1        

        return ans