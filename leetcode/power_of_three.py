class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        import math
        return ( math.log(n)/math.log(3) ) % 1


s = Solution()
k = s.isPowerOfThree(21)
print(k)