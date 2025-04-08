class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pos, ans = [], []
        ln = len(boxes)
        
        for i in range(ln):
            if boxes[i] == '1':
                pos.append(i)
                
        for i in range(ln):
            sm = 0
            for idx in pos:
                dst = abs(i - idx)
                sm += dst
            ans.append(sm)
        return ans