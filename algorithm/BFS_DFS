# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: 
            return 0
        queue = deque([(root, 1)])
        max_depth = 0
        
        while(queue):
            node, cntDepth = queue.popleft()
            if not node: 
                continue
            max_depth = max(max_depth, cntDepth)
            for child in node.children:
                queue.append((child, cntDepth+1))
            
        return max_depth
