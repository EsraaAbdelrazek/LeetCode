class Solution:
    def maxRemoval(self, nums, queries):
        n = len(nums)

        # Step 2: Heaps for applied and available queries
        used_query = []   # min-heap
        available_query = []  # max-heap

        # Step 1: Sort queries by start
        queries.sort(key=lambda x: x[0])
        query_pos = 0
        applied_count = 0

        # Step 3: Traverse nums
        for i in range(n):
            # Step 3a: Add queries starting at i
            while query_pos < len(queries) and queries[query_pos][0] == i:
                heapq.heappush(available_query, -queries[query_pos][1])
                query_pos += 1

            # Step 3b: Subtract active query count
            nums[i] -= len(used_query)

            # Step 3c: Apply more if needed
            while nums[i] > 0 and available_query and -available_query[0] >= i:
                heapq.heappush(used_query, -heapq.heappop(available_query))
                nums[i] -= 1
                applied_count += 1

            # Step 3d: Fail if nums[i] > 0
            if nums[i] > 0:
                return -1

            # Step 3e: Remove expired
            while used_query and used_query[0] == i:
                heapq.heappop(used_query)

        # Step 4: Return result
        return len(queries) - applied_count