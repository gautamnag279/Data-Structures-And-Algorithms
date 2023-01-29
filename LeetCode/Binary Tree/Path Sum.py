# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum and not (root.left or root.right):
            return True
        
        sum -= root.val
        
        return self.hasPathSum(root.left , sum) or self.hasPathSum(root.right , sum)
        
