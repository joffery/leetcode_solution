# Definition for a binary tree node.
# class TreeNode(object)
#     def __init__(self, x)
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object)
    def maxDepth(self, root)
        
        type root TreeNode
        rtype int
        
        if not root
            return 0
        
        if root.left and root.right
            return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        elif root.left
            return self.maxDepth(root.left)+1
        else
            return self.maxDepth(root.right)+1