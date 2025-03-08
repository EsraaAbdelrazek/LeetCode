class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_ops = float('inf')

        current_w_count = sum(1 for i in range(k) if blocks[i] == 'W')
        min_ops = current_w_count

      
        for i in range(k, n):
            if blocks[i - k] == 'W':  
                current_w_count -= 1
            if blocks[i] == 'W':  
                current_w_count += 1
            
            min_ops = min(min_ops, current_w_count)

        return min_ops
