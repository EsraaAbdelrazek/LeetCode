class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Building augmented graph
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))  # Reverse edge

        # Initialize distance array from 0 node
        dist = [math.inf] * n
        dist[0] = 0

        # Dijkstra
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if u == n - 1:  # Early exit
                return d
            if d != dist[u]:  # Stale edge
                continue
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:  # Edge relaxation
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        # No path found
        return -1