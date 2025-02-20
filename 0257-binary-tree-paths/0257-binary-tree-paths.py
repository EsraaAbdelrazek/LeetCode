from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if not root:  # Check if root is None before calling dfs
        #     return []
        
        def dfs(node: TreeNode, path: str):
            if not node:  
                return
            
            path += str(node.val)

            if not node.left and not node.right:  
                result.append(path)
            else:
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)  

        result = []
        dfs(root, "")
        return result
