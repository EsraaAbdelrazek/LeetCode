class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:            
        hFences.extend([1, m]) ; vFences.extend([1, n])
        hFences.sort()         ; vFences.sort()
        
        if len(hFences) > len(vFences):
            hFences, vFences = vFences, hFences

        hs = set()
        for i in range(1, len(hFences)):
            e = hFences[i]
            hs.update(e - s for s in hFences[:i])

        ans = 0
        for i in range(1, len(vFences)):
            e = vFences[i]
            if e < ans:
                break
            for j in range(i):
                s = e - vFences[j]
                if s in hs:
                    ans = max(ans, s)
                    break

        if not ans:
            return -1
        return pow(ans, 2, 10**9 + 7)