class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        n, edges = len(points), [] 

        for (x1, y1), (x2, y2) in combinations(points, 2):

            a, b = y1 - y2, x2 - x1
            length = a * a + b * b

            if a < 0 or (a == 0 and b < 0):
                a, b = -a, -b
            
            a,b = a//gcd(a,b), b//gcd(a,b)
            c = a * x1 + b * y1

            edges.append((a,b,c,length))


        edges.sort()       
        trapCnt, newTrapCnt, trapezoids = 0, 1, 0

        for edge1, edge2 in pairwise(edges):

            if edge1[:3] == edge2[:3]:
                newTrapCnt += 1

            elif edge1[:2] == edge2[:2]:
                trapezoids+= trapCnt * newTrapCnt
                trapCnt+= newTrapCnt
                newTrapCnt = 1

            else:
                trapezoids += trapCnt * newTrapCnt
                trapCnt, newTrapCnt = 0, 1

        trapezoids+= trapCnt * newTrapCnt
        

        edges.sort(key = lambda x: x[3])  
        paraCnt, newParaCnt, parallelograms = 0, 1, 0

        for edge1, edge2 in pairwise(edges):
            
            if edge1 == edge2:
                newParaCnt += 1

            elif (edge1[:2],edge1[3]) == (edge2[:2],edge2[3]):
                parallelograms += paraCnt * newParaCnt
                paraCnt += newParaCnt
                newParaCnt = 1
                
            else:
                parallelograms+= paraCnt * newParaCnt
                paraCnt, newParaCnt = 0, 1

        parallelograms+= paraCnt * newParaCnt
        paraCnt+= newParaCnt


        return trapezoids - parallelograms//2  