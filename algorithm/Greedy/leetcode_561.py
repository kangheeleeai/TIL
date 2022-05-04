# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        answer = 0
        for i in range(1, len(sorted_nums)+1, 2):
            answer += min(sorted_nums[i-1:i+1])
        return answer
