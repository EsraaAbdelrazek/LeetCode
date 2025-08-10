class Solution:
 def subarrayBitwiseORs(_,a):
  r=s=set()
  for x in a:s={x|y for y in s}|{x};r|=s
  return len(r)