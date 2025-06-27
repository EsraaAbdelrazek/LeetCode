class Solution:
    def longestSubsequenceRepeatedK(self, s: str, K: int) -> str:
        n = len(s)

        # Step 1: Preprocessing - Build nextPos table
        #         nextPos[i][c] = next index ≥ i where char 'a'+c appears
        nextPos = [[n] * 26 for _ in range(n + 2)]

        # Step 1.1: Initialize final rows to sentinel n
        for c in range(26):
            nextPos[n][c] = nextPos[n + 1][c] = n

        # Step 1.2: Fill table from right to left
        for i in range(n - 1, -1, -1):
            for c in range(26):
                nextPos[i][c] = nextPos[i + 1][c]
            nextPos[i][ord(s[i]) - ord('a')] = i

        # Step 2: Binary Search on length of repeated subsequence
        low, high = 1, n // K
        res = ""

        while low <= high:
            mid = (low + high) // 2

            # Step 2.1: Try to build subsequence of length `mid` using DFS
            found = self.dfsTry(mid, K, 0, [''] * mid, s, nextPos)
            if found:
                res = found
                low = mid + 1
            else:
                high = mid - 1

        return res

    # Step 3: DFS - Build lexicographically largest subsequence of length `len`
    def dfsTry(self, length, K, idx, path, s, nextPos):
        if idx == length:
            return ''.join(path) if self.canExtend(path, length, s, nextPos, K) else None

        for c in reversed(range(26)):
            path[idx] = chr(ord('a') + c)

            if self.canExtend(path, idx + 1, s, nextPos, K):
                result = self.dfsTry(length, K, idx + 1, path, s, nextPos)
                if result:
                    return result

        return None

    # Step 4: Check if (prefix of length d) * K is a subsequence of s
    def canExtend(self, path, d, s, nextPos, K):
        pos = 0
        n = len(s)

        for _ in range(K):
            for i in range(d):
                c = ord(path[i]) - ord('a')
                if pos >= n:
                    return False
                pos = nextPos[pos][c]
                if pos == n:
                    return False
                pos += 1
        return True