class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            if rank[pa] == rank[pb]:
                rank[pa] += 1

        for a, b in allowedSwaps:
            unite(a, b)

        from collections import defaultdict

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        ans = 0

        for idxs in groups.values():
            freq = {}

            for i in idxs:
                freq[source[i]] = freq.get(source[i], 0) + 1

            for i in idxs:
                if freq.get(target[i], 0) > 0:
                    freq[target[i]] -= 1
                else:
                    ans += 1

        return ans