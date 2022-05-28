# https://leetcode.com/problems/sqrtx
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        answer = 0
        for i in range(1, (x//2)+1):
            pow_i=i*i
            if pow_i == x:
                return i
            elif pow_i < x:
                answer = i
            else:
                return answer
        return answer
