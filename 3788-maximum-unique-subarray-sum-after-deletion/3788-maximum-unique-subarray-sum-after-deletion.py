class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum = 0
        st = set()
        mxNeg = float('-inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                st.add(nums[i])
            else:
                mxNeg = max(mxNeg, nums[i])
        for val in st:
            sum += val
        if len(st) > 0:
            return sum
        else:
            return mxNeg