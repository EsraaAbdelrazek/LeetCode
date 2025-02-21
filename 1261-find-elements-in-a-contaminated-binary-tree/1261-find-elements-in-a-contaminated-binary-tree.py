# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        
            self.s = set ([0]) 
            root.val = 0 

            def dfs (node) : 
                if node : 
                    if node.left : 
                        node .left.val = node .val *2 +1  
                        self .s.add (node.left .val) 

                    if node .right : 
                        node .right .val = node .val *2 +2  
                        self .s.add (node . right .val) 

                    dfs (node.left) 
                    dfs (node .right) 

            dfs (root)


    def find(self, target: int) -> bool:
        return target in self.s 

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)