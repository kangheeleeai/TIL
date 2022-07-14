# https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x: x[0])
        n = len(pairs)
        answer = [pairs[0]]
        
        for i in range(1, n):
            if answer[-1][1] >= pairs[i][0]:
                if answer[-1][1] >= pairs[i][1]:
                    answer.pop()
                    answer.append(pairs[i])
            else:
                answer.append(pairs[i])
                
        return len(answer)

    
