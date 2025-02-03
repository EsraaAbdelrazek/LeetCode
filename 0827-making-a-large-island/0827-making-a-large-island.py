from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # Start island IDs from 2 (since grid has 0s and 1s)
        island_sizes = {0: 0}  # Dictionary to store island sizes

        # Directions for 4-way connectivity
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, island_id):
            """DFS to mark and count island size."""
            if not (0 <= r < n and 0 <= c < n) or grid[r][c] != 1:
                return 0
            grid[r][c] = island_id  # Mark cell with island ID
            size = 1
            for dr, dc in directions:
                size += dfs(r + dr, c + dc, island_id)
            return size

        # Step 1: Find all islands and assign them unique IDs
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1

        max_island = max(island_sizes.values() or [0])  # Get the max existing island size

        # Step 2: Try flipping each zero and compute the possible island size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    new_size = 1  # Flipping this zero to one

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])  # Add adjacent island IDs

                    for island in seen:
                        new_size += island_sizes[island]

                    max_island = max(max_island, new_size)

        return max_island
