class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = prices [0] 
        profit = 0 
        for price in prices [1 :]: 
            if price < cur :
                 cur = price 
            else : 
                profit = max (profit , price - cur)

        return profit