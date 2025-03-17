class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
#         This sorts nums in-place with a custom sort key:
#            hashmap[x]: Sort by frequency (ascending).
#            -x: If two elements have the same frequency, sort by value descending. 
        nums.sort(key=lambda x: (hashmap[x], -x))
        return nums

        