# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: 
            return []
        answer = []
        queue = deque([root])
        sum_result, size, count = 0, 1, 1
        while queue:
            node = queue.popleft()
            sum_result += node.val
            size -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if size == 0:
                answer.append(sum_result / count)
                size = count = len(queue)
                sum_result = 0
        return answer
            
