# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def isBadVersion(version):
    return True if version > 5 else False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l = 0
        h = n
        while l<=h:
            m = (l+h)>>1
            if isBadVersion(m):
                h=m-1
            else:
                l=m+1

        return l


s = Solution()
k = s.firstBadVersion(4)
print(k)