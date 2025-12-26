class Solution:
    def bestClosingTime(self, s: str) -> int:
        return -max(zip(accumulate((2*(c=='Y')-1 for c in s),
            initial=0),count(step=-1)))[1]