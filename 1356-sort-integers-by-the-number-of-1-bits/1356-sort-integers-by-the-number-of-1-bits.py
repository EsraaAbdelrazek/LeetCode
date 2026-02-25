class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bitmap = collections.defaultdict(list)
        
        for val in arr:
            bits = val.bit_count()
            bitmap[bits].append(val)
            
        ans = []
        for key in sorted(bitmap.keys()):
            for val in sorted(bitmap[key]):
                ans.append(val)
                
        return ans