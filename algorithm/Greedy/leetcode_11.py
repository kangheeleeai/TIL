#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        answer = 0
        for h in range(1, max(height)+1):
            while True:
                if height[l] < h:
                    l+=1
                else:
                    break
            while True:
                if height[r] < h:
                    r-=1
                else:
                    break
            water = h * (r-l)
            if answer < water:
                answer = water
        return answer
