# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        def diameter(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            self.maximum = max(self.maximum, left + right)
            return 1 + max(left, right)
        
        diameter(root)
        return self.maximum