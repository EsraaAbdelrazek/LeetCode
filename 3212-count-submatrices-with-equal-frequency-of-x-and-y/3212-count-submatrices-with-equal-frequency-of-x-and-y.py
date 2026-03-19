class Solution:
    def numberOfSubmatrices(self, g: List[List[str]]) -> int:
        p = (accumulate(map({'X':1,'Y':1j,'.':0}.get,r)) for r in g)
        return sum(0<q.real==q.imag for c in zip(*p) for q in accumulate(c))