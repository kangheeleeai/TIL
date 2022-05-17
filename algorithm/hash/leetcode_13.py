# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {"I":1,
                       "V":5,
                       "X":10,
                       "L":50,
                       "C":100,
                       "D":500,
                       "M":1000}
        num = 0
        flag = 0
        for i in range(len(s)-1, -1, -1):
            if symbol_dict[s[i]] >= flag:
                num += symbol_dict[s[i]]
            else:
                num -= symbol_dict[s[i]]
            flag = symbol_dict[s[i]]
        return num
