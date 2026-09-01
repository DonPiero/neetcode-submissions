# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.first = []
        self.second = []
        def arrayMaker(current, arr):
            if current == None:
                arr.append(None)
                return
            arr.append(current.val)
            arrayMaker(current.left, arr)
            arrayMaker(current.right, arr)

        arrayMaker(root, self.first)
        arrayMaker(subRoot, self.second)
        diff = len(self.first) - len(self.second)
        if diff < 0:
            return False
        for i in range(diff + 1):
            if self.second == self.first[i:(i+len(self.second))]:
                return True
        return False

        