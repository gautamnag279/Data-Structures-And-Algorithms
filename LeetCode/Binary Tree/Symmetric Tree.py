# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False
        if p == None and q == None:
            return True
        if p.val != q.val:
            return False
        return self.compare(p.left,q.right) and self.compare(p.right,q.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.compare(root.left,root.right)
    
