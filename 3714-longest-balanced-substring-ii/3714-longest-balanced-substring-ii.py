class Solution:
    def longestBalanced(self, s: str) -> int:
        results = [
            self._solve1(s, 'a'),
            self._solve1(s, 'b'),
            self._solve1(s, 'c'),
            self._solve2(s, 'a', 'b'),
            self._solve2(s, 'a', 'c'),
            self._solve2(s, 'b', 'c'),
            self._solve3(s),
        ]
        return max(results)

    def _solve1(self, s: str, t: str) -> int:
        result = 0
        count = 0
        for c in s:
            if c == t:
                count += 1
                if count > result:
                    result = count
            else:
                count = 0
        return result

    def _solve2(self, s: str, t1: str, t2: str) -> int:
        result = 0
        counts0 = 0
        counts1 = 0
        previous = {}
        for i, c in enumerate(s):
            if c != t1 and c != t2:
                previous.clear()
                counts0 = 0
                counts1 = 0
            else:
                if c == t1:
                    counts0 += 1
                else:
                    counts1 += 1
                if counts0 == counts1:
                    v = counts0 * 2
                    if v > result:
                        result = v
                else:
                    diff = counts0 - counts1
                    if diff in previous:
                        v = i - previous[diff]
                        if v > result:
                            result = v
                    else:
                        previous[diff] = i
        return result

    def _solve3(self, s: str) -> int:
        result = 0
        ca = cb = cc = 0
        previous = {}
        for i, ch in enumerate(s):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1
            if ca == cb and cb == cc:
                result = i + 1
            else:
                diff = (ca - cb) * 100001 + (cb - cc)
                if diff in previous:
                    v = i - previous[diff]
                    if v > result:
                        result = v
                else:
                    previous[diff] = i
        return result