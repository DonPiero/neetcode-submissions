# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def checker(current): 
            if current == None:
                return 0
            left = checker(current.left)
            right = checker(current.right)
            diff = left - right
            if diff < -1 or diff > 1:
                self.result = False
            return 1 + max(left, right)

        checker(root)
        return self.result
