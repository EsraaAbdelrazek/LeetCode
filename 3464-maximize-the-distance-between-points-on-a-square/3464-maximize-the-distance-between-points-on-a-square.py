class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:

        def flatten(p):
            x, y = p
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 3 * side - x
            return 4 * side - y

        arr = sorted(flatten(p) for p in points)
        n = len(arr)

        def notValid(d):
            for i in range(n):
                ptr = i
                cnt = 1

                while cnt < k:
                    target = arr[ptr] + d

                    import bisect
                    j = bisect.bisect_left(arr, target)

                    if j == n:
                        break

                    ptr = j
                    cnt += 1

                    if d + arr[ptr] > arr[i] + 4 * side:
                        cnt = 0
                        break

                if cnt == k:
                    return False

            return True

        low, high = 0, side
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if not notValid(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans