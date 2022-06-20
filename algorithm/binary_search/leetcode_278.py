#   https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = n
        l, h = 0, n+1

        while l < h:
            m = l + (h-l)//2
            if isBadVersion(m):
                if m < f:
                    f = m
                h = m
            else:
                l = m+1

        return f
