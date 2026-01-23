class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        
        array = [int(x) for x in nums]
        left = list(range(-1, N - 1))
        right = list(range(1, N + 1))
        
        flipped = 0
        pairSum = SortedList()
        
        def add(i, N, array):
            nonlocal flipped
            if 0 <= i < N:
                j = right[i]
                if j < N:
                    pairSum.add([array[i] + array[j], i])
                    if array[i] > array[j]:
                        flipped += 1
                        
        def remove(i, N, array):
            nonlocal flipped
            if 0 <= i < N:
                j = right[i]
                if j < N:
                    if array[i] > array[j]:
                        flipped -= 1
                    pairSum.discard([array[i] + array[j], i])

        for i in range(N - 1):
            if array[i] > array[i + 1]:
                flipped += 1
            pairSum.add([array[i] + array[i + 1], i])
            
        op = 0
        
        while flipped > 0 and pairSum:
            s, i = pairSum.pop(0)
            
            j = right[i]
            h = left[i]
            k = right[j]
            
            remove(h, N, array)
            if array[i] > array[j]:
                flipped -= 1
            remove(j, N, array)
            
            array[i] += array[j]
            op += 1
            
            right[i] = k
            if k < N:
                left[k] = i
                
            add(h, N, array)
            add(i, N, array)
            
        return op