# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        less_num = list(map(lambda x: target-x, nums))
        answer = list()
        for idx, i in enumerate(less_num):
            if i in nums:
                if idx != nums.index(i):
                    answer.append(idx)
                    answer.append(nums.index(i))
                    break
        return answer
