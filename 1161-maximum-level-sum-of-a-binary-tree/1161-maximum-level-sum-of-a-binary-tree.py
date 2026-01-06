# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(int)

        def bfs(root,level):
            if not root:
                return
            levels[level] += root.val
            bfs(root.left,level+1)
            bfs(root.right,level+1)
            return
        bfs(root,1)
        return max(levels,key=levels.get)