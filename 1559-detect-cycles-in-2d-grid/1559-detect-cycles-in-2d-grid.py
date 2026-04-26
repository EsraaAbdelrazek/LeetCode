class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visit = [False] * (m * n)
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))

        def dfs(r, c, pr, pc):
            visit[r * n + c] = True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (nr, nc) != (pr, pc):
                    if 0 <= nr < m:
                        if 0 <= nc < n:
                            if grid[nr][nc] == grid[r][c]:
                                if visit[nr * n + nc]:
                                    return True
                                if dfs(nr, nc, r, c):
                                    return True
            return False

        for i in range(m):
            for j in range(n):
                if not visit[i * n + j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False