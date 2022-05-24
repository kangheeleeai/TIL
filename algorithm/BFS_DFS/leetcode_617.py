#https://leetcode.com/problems/merge-two-binary-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root1 , root2):
        if(root1 == None and root2 == None):
            return None 
        elif(root1 == None and root2 != None):
            return root2 
        elif(root1 != None and root2 == None):
            return root1 
        root = TreeNode(root1.val + root2.val)
        root.left = self.dfs(root1.left , root2.left)
        root.right = self.dfs(root1.right , root2.right)
        return root 
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root1 , root2)
