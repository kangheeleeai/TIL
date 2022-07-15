# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_mirror(self, l_tree, r_tree):
        if l_tree is None and r_tree is None:
            return True
        elif l_tree is None or r_tree is None:
            return False
        else:
            if l_tree.val != r_tree.val:
                return False
            else:
                return self.check_mirror(l_tree.left, r_tree.right) and self.check_mirror(l_tree.right, r_tree.left)
            
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.check_mirror(root.left, root.right)

    
