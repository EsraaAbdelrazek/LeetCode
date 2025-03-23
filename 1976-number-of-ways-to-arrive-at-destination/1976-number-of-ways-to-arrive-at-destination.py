class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        from heapq import heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Build the graph as an adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Step 2: Initialize Dijkstra's Algorithm
        dist = [float('inf')] * n  # Shortest distance to each node
        ways = [0] * n  # Number of ways to reach each node in shortest time
        min_heap = [(0, 0)]  # (time, node)
        
        dist[0] = 0
        ways[0] = 1
        
        while min_heap:
            time, node = heappop(min_heap)
            
            # Ignore outdated distance
            if time > dist[node]:
                continue
            
            # Step 3: Explore neighbors
            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time
                
                # Found a shorter path
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]  # Reset paths count
                    heappush(min_heap, (new_time, neighbor))
                
                # Found another shortest path
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        # Step 4: Return the number of ways to reach node (n-1)
        return ways[n-1]
