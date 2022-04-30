# https://leetcode.com/problems/di-string-match/submissions/

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer_list = []
        l = 0
        r = len(s)
        for char in s:
            if char == 'I':
                answer_list.append(l)
                l += 1
            else:
                answer_list.append(r)
                r -= 1
        
        answer_list.append(l)
        return answer_list
