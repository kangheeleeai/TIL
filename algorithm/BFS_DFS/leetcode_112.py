# https://leetcode.com/problems/path-sum/
Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum_num):
            if not node:
                return False
            sum_num += node.val
            if not node.left and not node.right:
                return sum_num == targetSum
            return (dfs(node.left, sum_num) or (dfs(node.right, sum_num)))
        return dfs(root, 0)
