class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        emp = numBottles
        while emp >= numExchange:
            emp -= numExchange
            res += 1
            emp += 1
            numExchange += 1
        return res