class SegTree:
    def __init__(self, n: int):
        self.n = 1 << n.bit_length()
        self.tree = [0] * (self.n*2)
    def update(self, index: int, val: int):
        index += self.n
        self.tree[index] = val
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])
    def query(self, index: int) -> int:
        index += self.n
        res = self.tree[index]
        while index > 1:
            if index % 2 == 1:
                res = max(res, self.tree[index - 1])
            index //= 2
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        Sorted = SortedList()
        inter = SegTree(max(q[1] for q in queries))
        res = []
        Sorted.add(0)
        inter.update(0, 0)
        for q in queries:
            if q[0] == 1:
                idx = Sorted.bisect(q[1])
                if idx < len(Sorted):
                    nxt = Sorted[idx]
                    inter.update(nxt, nxt - q[1])
                inter.update(q[1], q[1] - Sorted[idx - 1])
                Sorted.add(q[1])
            else:
                prev = Sorted[Sorted.bisect(q[1]) - 1]
                mx = max(q[1] - prev, inter.query(prev))
                res.append(q[2] <= mx)
        return res