# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        hash_list = list()
        while True:
            if n == 1:
                return True
            temp = 0
            for s in str(n):
                temp += pow(int(s), 2)
            if temp in hash_list:
                return False
            else:
                hash_list.append(temp)
            n = temp
            
