class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
      

        events.sort()
        heap = []
        i = 0
        day = 1
        count = 0
        n = len(events)
        while i < n or heap:
            while i < n and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                count += 1
            day += 1
        return count        