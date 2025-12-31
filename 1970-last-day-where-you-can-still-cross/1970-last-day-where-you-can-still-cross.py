class Solution(object):
    def latestDayToCross(self, row, col, cells):
        n = row * col
        top, bottom = n, n + 1
        parent = list(range(n + 2))
        rank = [0] * (n + 2)
        land = [False] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a, b):
            a, b = find(a), find(b)
            if a == b: return
            if rank[a] < rank[b]: parent[a] = b
            elif rank[a] > rank[b]: parent[b] = a
            else: parent[b] = a; rank[a] += 1

        for d in range(len(cells) - 1, -1, -1):
            r, c = cells[d][0] - 1, cells[d][1] - 1
            id = r * col + c
            land[id] = True

            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    nid = nr * col + nc
                    if land[nid]:
                        unite(id, nid)

            if r == 0: unite(id, top)
            if r == row - 1: unite(id, bottom)

            if find(top) == find(bottom):
                return d
        return 0