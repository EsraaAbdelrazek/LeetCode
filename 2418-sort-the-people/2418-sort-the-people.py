# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         n = len(names)
#         indices = list(range(n))
        
#         # Sort indices based on heights in descending order
#         indices.sort(key=lambda i: heights[i], reverse=True)
        
#         # Build result based on sorted indices
#         result = [names[i] for i in indices]
#         return result
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True, key=lambda x: x[0])
        sorted_names = [name for height, name in people]
        return sorted_names