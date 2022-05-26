# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_splits = s.split()
        return len(s_splits[-1])
