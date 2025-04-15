from typing import List

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, index, value):
        index += 1  # BIT is 1-indexed
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Map value to index in nums2
        pos2 = [0] * n
        for i in range(n):
            pos2[nums2[i]] = i

        # Transform nums1 to mapped indices in nums2
        mapped = [pos2[val] for val in nums1]

        left_tree = FenwickTree(n)
        right_tree = FenwickTree(n)

        # Fill right tree
        for val in mapped:
            right_tree.update(val, 1)

        total_triplets = 0

        for j in range(n):
            mid_val = mapped[j]
            right_tree.update(mid_val, -1)

            left_smaller = left_tree.query(mid_val - 1)
            right_greater = right_tree.query(n - 1) - right_tree.query(mid_val)

            total_triplets += left_smaller * right_greater

            left_tree.update(mid_val, 1)

        return total_triplets