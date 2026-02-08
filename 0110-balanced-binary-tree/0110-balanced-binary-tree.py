class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_diff = 0
        
        def helper(node, depth):
            if not node:
                return depth
            
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            
            self.max_diff = max(self.max_diff, abs(left - right))
            
            return max(left, right)
            
        helper(root, 0)
        return self.max_diff <= 1