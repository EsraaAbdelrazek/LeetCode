class Solution:
    def digits(self, x):
        cnt = 0
        while x > 0:
            cnt += 1
            x //= 10
        return cnt

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # storing all prefixes of arr1
        for num in arr1:
            x = num
            while x > 0:
                prefixes.add(x)
                x //= 10

        ans = 0

        # check prefixes of arr2 numbers
        for num in arr2:
            x = num
            len_ = self.digits(num)

            # checking from larger => smaller
            while x > 0:
                if x in prefixes:
                    ans = max(ans, len_)
                    # first match is the longest
                    # so we stop
                    break

                x //= 10
                len_ -= 1

        return ans