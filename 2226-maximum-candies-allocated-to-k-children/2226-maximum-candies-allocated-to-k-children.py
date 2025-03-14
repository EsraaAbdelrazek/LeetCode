class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:  # If total candies are less than k, return 0
              return 0
    
        low, high = 1, max(candies)
        best = 0
        
        while low <= high:
            mid = (low + high) // 2
            count = sum(c // mid for c in candies)  # Total children that can receive 'mid' candies
            
            if count >= k:  # If we can serve at least k children
                best = mid  # Update best answer
                low = mid + 1  # Try for a larger size
            else:
                high = mid - 1  # Try a smaller size
                
        return best
        