class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
      
        xor = 0
        for num in nums:
            xor ^= num

        # Find rightmost set bit
        diff_bit = xor & -xor

        a = 0
        b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]

# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         hashmap = Counter(nums)
#         ans = []
#         print(hashmap)
#         for key, value in hashmap.items():
#             if value == 1:
#                 ans.append(key)
#         print(ans)
#         return ans
            