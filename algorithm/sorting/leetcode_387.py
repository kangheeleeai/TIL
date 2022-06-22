# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c_list=list()
        idx_list=list()
        for idx, c in enumerate(s):
            if c in c_list:
                idx_list[c_list.index(c)]=-1
            if c not in c_list:
                c_list.append(c)
                idx_list.append(idx)
        answer=list(filter((-1).__ne__, idx_list))
        if not answer:
            return -1
        else:
            return min(answer)
