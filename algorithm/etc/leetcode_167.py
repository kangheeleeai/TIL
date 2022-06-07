# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = list()
        for idx, i in enumerate(numbers):
            less_num = target-i
            if less_num in numbers:
                answer.append(idx+1)
                less_idx = numbers.index(less_num)
                if idx == less_idx:
                    answer.append(idx+2)
                else:
                    answer.append(less_idx+1)
                break
        return answer
