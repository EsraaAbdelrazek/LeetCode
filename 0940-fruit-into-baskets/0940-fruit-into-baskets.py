class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        res = 0
        wstart = 0
        curr = 0
        for wend in range(len(fruits)):
            fruit = fruits[wend]
            if fruit not in dic:
                dic[fruit] = 0
            dic[fruit] += 1
            while len(dic) > 2 and wstart < wend:
                rfruit = fruits[wstart]
                dic[rfruit] -= 1
                if dic[rfruit] == 0:
                    del dic[rfruit]
                wstart += 1
            res = max(wend-wstart+1, res)
            
        return res