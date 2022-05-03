# https://leetcode.com/problems/queue-reconstruction-by-height/
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:x[1])
        people.sort(reverse = True, key = lambda x:x[0])
        answer = list()
        
        for h, k in people:
            if not answer:
                answer.append([h, k])
                continue
            else:
                answer.insert(k, [h, k])
        return answer
