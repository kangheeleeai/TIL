# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l_tree = self.maxDepth(root.left)
        r_tree = self.maxDepth(root.right)
        return max(l_tree, r_tree) + 1
