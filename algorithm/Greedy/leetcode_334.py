# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        least1=float('inf')
        least2=float('inf')
        for num in nums:
            if num<=least1:
                least1=num
            elif num<=least2:
                least2=num
            else:
                return True
        return False
