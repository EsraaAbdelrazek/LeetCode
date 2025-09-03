import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
       # Function to compute marginal gain
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # Max heap (Python heapq is min-heap, so we store negative gains)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Assign extra students
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute final average ratio
        total_ratio = sum(p / t for _, p, t in heap)
        return total_ratio / len(classes)