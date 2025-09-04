class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        person1 = abs(x - z)
        person2 = abs(y - z)
        
        if person1 < person2:
            return 1
        elif person2 < person1:
            return 2
        else:
            return 0
        