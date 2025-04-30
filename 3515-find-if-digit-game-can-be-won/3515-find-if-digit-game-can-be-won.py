class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        Asingle = sum(x for x in nums if x <10)
        Adouble = sum(x for x in nums if 10 <= x < 100)
        
        total = sum (nums)

        Bdouble = total - Adouble
        Bsingle=  total - Asingle

        return Asingle > Bsingle or Adouble > Bdouble 