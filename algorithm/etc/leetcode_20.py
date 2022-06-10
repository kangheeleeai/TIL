#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        in_=["(", "[", "{"]
        out_=[")", "]", "}"]
        answer=list()
        for c in s:
            if c in in_:
                answer.append(c)
            else:
                if not answer:
                    return False
                elif in_.index(answer[-1]) == out_.index(c):
                    answer.pop()
                else:
                    return False
        if not answer:
            return True
        else:
            return False
