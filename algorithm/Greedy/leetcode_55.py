#https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        answer = False
        minimun = 1
        nums = reversed(nums)
        for idx, num in enumerate(nums):
            if idx==0:
                continue
            if num>=minimun:
                answer=True
                minimun = 1
            else:
                answer=False
                minimun += 1
                
        return answer
