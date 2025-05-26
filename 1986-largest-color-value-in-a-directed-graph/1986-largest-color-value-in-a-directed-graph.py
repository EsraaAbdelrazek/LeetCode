# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         hashmap = collections.defaultdict(list)

#         for u, v in edges:
#             if u == v:
#                 return -1
#             hashmap[u].append(v)

#         visited = set()
        
#         @cache
#         def dfs(curr, target):
#             result = 0
#             for adj in hashmap[curr]:
#                 if adj in visited:
#                     return float('inf')
#                 visited.add(adj)
#                 result = max(result, dfs(adj, target))
#                 visited.remove(adj)

#             return result + 1 if colors[curr] == target else result

#         max_path_value = 0
#         for i in range(len(colors)):
#             max_path_value = max(max_path_value, dfs(i, colors[i]))

#         return -1 if max_path_value == float('inf') else max_path_value

from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # color count per node: dp[node][c] = max freq of color 'a'+c in any path ending at node
        dp = [[0] * 26 for _ in range(n)]

        # queue for topological sort
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        visited_count = 0
        res = 0

        while q:
            node = q.popleft()
            visited_count += 1
            color_index = ord(colors[node]) - ord('a')
            dp[node][color_index] += 1
            res = max(res, dp[node][color_index])

            for nei in graph[node]:
                for c in range(26):
                    dp[nei][c] = max(dp[nei][c], dp[node][c])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if visited_count == n else -1  # if not all nodes visited → cycle
