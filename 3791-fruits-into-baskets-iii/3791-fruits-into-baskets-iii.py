class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        self.seg = [0] * (4 * n)
        self.build(baskets, 0, 0, n - 1)

        unplaced = 0
        for fruit in fruits:
            if self.seg[0] < fruit:
                unplaced += 1
            else:
                if not self.place(0, 0, n - 1, fruit):
                    unplaced += 1
        return unplaced

    def build(self, baskets, idx, l, r):
        if l == r:
            self.seg[idx] = baskets[l]
            return self.seg[idx]
        mid = (l + r) // 2
        left = self.build(baskets, 2 * idx + 1, l, mid)
        right = self.build(baskets, 2 * idx + 2, mid + 1, r)
        self.seg[idx] = max(left, right)
        return self.seg[idx]

    def place(self, idx, l, r, val):
        if self.seg[idx] < val:
            return False
        if l == r:
            self.seg[idx] = -1
            return True
        mid = (l + r) // 2
        placed = self.place(2 * idx + 1, l, mid, val)
        if not placed:
            placed = self.place(2 * idx + 2, mid + 1, r, val)
        self.seg[idx] = max(self.seg[2 * idx + 1], self.seg[2 * idx + 2])
        return placed