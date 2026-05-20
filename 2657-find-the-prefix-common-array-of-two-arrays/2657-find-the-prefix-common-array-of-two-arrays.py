class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        mp = {}

        count = 0

        for i in range(len(A)):
            if A[i] == B[i]:
                mp[A[i]] = mp.get(A[i], 0) + 2
                count += 1
            else:
                mp[A[i]] = mp.get(A[i], 0) + 1
                mp[B[i]] = mp.get(B[i], 0) + 1

                if mp[A[i]] == 2:
                    count += 1

                if mp[B[i]] == 2:
                    count += 1

            A[i] = count

        return A