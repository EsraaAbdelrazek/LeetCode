class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arry = set (arr)
        res = 0 
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                lth = 2 
                while nxt in arry : 
                    lth += 1 
                    prev , cur = cur , nxt 
                    nxt = prev + cur 
                    res = max (res , lth )

        return res