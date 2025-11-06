class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        g,d = defaultdict(list),{}
        for v,u in connections: g[v].append(u); g[u].append(v)

        def dfs(v,sl):
            if v not in d:
                d[v] = sl; sl.add(v)
                for u in g[v]: dfs(u,sl)

        for v in range(1,c+1): dfs(v,SortedList())
        
        return [x in d[x] and x or d[x] and d[x][0] or -1 
            for op,x in queries if op==1 or d[x].discard(x)]