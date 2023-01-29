class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left , root.right = self.invertTree(root.right) , self.invertTree(root.left)
            return root
        
        
#This is he same code but it is easy to understand  
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:
            # General case:
            
            # invert child node of current root
            root.left, root.right = root.right, root.left
            
            # invert subtree with DFS
            
            if root.left:
                self.invertTree( root.left )
            
            if root.right:
                self.invertTree( root.right )
            
            return root
        
        else:
            # Base case:
            # empty tree
            
            return None
