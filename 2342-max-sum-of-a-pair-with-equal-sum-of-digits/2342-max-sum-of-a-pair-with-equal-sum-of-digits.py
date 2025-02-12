class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
             return sum(int(d) for d in str(n))

        digit_sum_map = defaultdict(list)
        max_sum = -1

        for num in nums:
            ds = digit_sum(num)
            digit_sum_map[ds].append(num)

        for num_list in digit_sum_map.values():
            if len(num_list) > 1:
                num_list.sort(reverse=True)  # Sort descending to get top two numbers
                max_sum = max(max_sum, num_list[0] + num_list[1])

        return max_sum
            