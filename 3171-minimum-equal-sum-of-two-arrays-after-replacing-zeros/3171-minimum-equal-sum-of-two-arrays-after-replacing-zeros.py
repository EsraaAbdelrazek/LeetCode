class Solution:
    def minSum(self, nums1, nums2):
        nums1_sum = sum(x if x != 0 else 1 for x in nums1)
        nums2_sum = sum(x if x != 0 else 1 for x in nums2)

        nums1_zeros = nums1.count(0)
        nums2_zeros = nums2.count(0)

        if (nums1_zeros == 0 and nums2_sum > nums1_sum) or \
           (nums2_zeros == 0 and nums1_sum > nums2_sum):
            return -1
        return max(nums1_sum, nums2_sum)