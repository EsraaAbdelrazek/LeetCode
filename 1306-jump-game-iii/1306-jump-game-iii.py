class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        q=deque()
        q.append(start)
        while q:
            i=q.pop()
            x=arr[i]
            if x==-1: continue #visited
            if x==0: return True
            arr[i]=-1
            if (l:=i-x)>=0 and arr[l]>=0: 
                q.append(l)
            if (r:=i+x)<n and arr[r]>=0: 
                q.append(r)
        return False