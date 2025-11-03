class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        intr_arr = zip(colors, neededTime)
        
        stack = deque()

        ans = 0
        for e in intr_arr:

            if(not stack):
                stack.append(e)
            else:

                if(stack[-1][0] != e[0]):
                    stack.append(e)
                
                else:

                    if(e[1] < stack[-1][1]):
                        ans += e[1]
                    
                    else:
                        popped = stack.pop()
                        stack.append(e)
                        ans += popped[1]
        
        return ans