class Solution:
    def maxCollectedFruits(self, g):
        n = len(g)
        return sum(g[i][i] for i in range(n)) + \
            (f:=cache(lambda i,j:0<=j<i<n and g[i][j]+max(f(i-1,j+1),f(i,j+1),f(i+1,j+1))))(n-1,0) + \
            (f:=cache(lambda i,j:0<=i<j<n and g[i][j]+max(f(i+1,j-1),f(i+1,j),f(i+1,j+1))))(0,n-1)