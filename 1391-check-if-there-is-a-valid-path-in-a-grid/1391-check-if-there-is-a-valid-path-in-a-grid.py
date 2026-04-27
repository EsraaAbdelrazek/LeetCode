class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs = {
            1: [(0,-1), (0,1)],
            2: [(1,0), (-1,0)],
            3: [(0,-1), (1,0)],
            4: [(1,0), (0,1)],
            5: [(-1,0), (0,-1)],
            6: [(-1,0), (0,1)]
        }

        m,n = len(grid), len(grid[0])
        visited = set()

        stack = [(0,0)]
        while stack:
            i,j = stack.pop()
            if i == m-1 and j == n-1:
                return True
            visited.add((i,j))
            for di, dj in dirs[grid[i][j]]:
                ni = i + di
                nj = j + dj
                if ni < 0 or nj < 0 or ni == m or nj == n or (ni, nj) in visited:
                    continue
                if (di * -1, dj * -1) in dirs[grid[ni][nj]]:
                    stack.append((ni, nj))
        return False