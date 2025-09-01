import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        # Max-heap using negative values since Python's heapq is min-heap
        pq = []
        for p, t in classes:
            gain = self.findGain(p, t)
            heapq.heappush(pq, (-gain, p, t))
        
        while extraStudents > 0:
            gain, p, t = heapq.heappop(pq)
            p += 1
            t += 1
            new_gain = self.findGain(p, t)
            heapq.heappush(pq, (-new_gain, p, t))
            extraStudents -= 1
        
        res = 0.0
        while pq:
            _, p, t = heapq.heappop(pq)
            res += p / t
        return res / len(classes)
    
    def findGain(self, p: int, t: int) -> float:
        return (p + 1) / (t + 1) - p / t