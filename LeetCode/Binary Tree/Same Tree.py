class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # base cases
        if not p and not q:  # when both trees are None
            return True
        elif not p or not q:  # When any of the tree is None
            return False
        
        # checking every node to be equal (root, left, right)
        # return True only when tree is same, else return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
