class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        x = Counter(nums) 
        pairs, rem = 0, 0 

        for count in x.values():
            pairs += count // 2
            rem += count % 2

        return [pairs, rem]