class Solution:
    MOD = 1000000007

    def modExp(self, base, exp):
        if exp == 0:
            return 1
        
        half = self.modExp(base, exp // 2)
        result = (half * half) % self.MOD

        if exp % 2:
            result = (result * base) % self.MOD

        return result

    def xorAfterQueries(self, arr, ops):
        n = len(arr)
        block = int(n ** 0.5) + 1

        buckets = [[] for _ in range(block)]

        for query in ops:
            left, right, step, val = query

            if step < block:
                buckets[step].append(query)
            else:
                pos = left
                while pos <= right:
                    arr[pos] = (arr[pos] * val) % self.MOD
                    pos += step

        for step in range(1, block):
            if not buckets[step]:
                continue

            multiplier = [1] * (n + step + 5)

            for query in buckets[step]:
                left, right, _, val = query

                lastIndex = left + ((right - left) // step) * step
                stop = lastIndex + step

                multiplier[left] = (multiplier[left] * val) % self.MOD

                invVal = self.modExp(val, self.MOD - 2)
                multiplier[stop] = (multiplier[stop] * invVal) % self.MOD

            for i in range(n):
                if i - step >= 0:
                    multiplier[i] = (multiplier[i] * multiplier[i - step]) % self.MOD

            for i in range(n):
                arr[i] = (arr[i] * multiplier[i]) % self.MOD

        ans = 0
        for value in arr:
            ans ^= value

        return ans