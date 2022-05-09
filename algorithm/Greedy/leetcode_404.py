# https://leetcode.com/problems/sum-of-left-leaves/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        answer = 0
        queue = [(root, 0)]
        
        while queue:
            node, l = queue.pop(0)
            if (not node.left) and (not node.right) and l:
                answer += node.val
            if node.left:
                queue.append((node.left, 1))
            if node.right:
                queue.append((node.right, 0))
        
        return answer
