#https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer=list()
        for idx, _ in enumerate(range(numRows)):
            if idx==0:
                answer.append([1])
            else:
                row=list()
                
                for i in range(len(answer[idx-1])):
                    if i==0:
                        row.append(1)
                    else:
                        row.append(answer[idx-1][i-1]+answer[idx-1][i])
                row.append(1)
                answer.append(row)
        return answer

    
