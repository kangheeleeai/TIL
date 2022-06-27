# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=list()
        if len(nums1)>len(nums2):
            for i in nums2:
                if i in nums1:
                    nums1.remove(i)
                    answer.append(i)
        else:
            for i in nums1:
                if i in nums2: 
                    nums2.remove(i)
                    answer.append(i)
        return 
