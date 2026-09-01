# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.aP = []
        self.aQ = []
        def arrayConstructor(current, result = []):
            if current == None:
                result.append(None)
                return 

            result.append(current.val)
            arrayConstructor(current.left, result)
            arrayConstructor(current.right, result)

        arrayConstructor(p, self.aP)
        arrayConstructor(q, self.aQ)

        return self.aP == self.aQ 
        