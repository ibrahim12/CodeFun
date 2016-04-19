class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        x = min(C, G) - max(A,E)
        y = min(D, H) - max(B, F)
        common = max(x,0) * max(y,0)

        return (A-C) * (B-D) + (E-G) * (F-H) - common



s = Solution()
k = s.computeArea(-3, 0, 3, 4, 0, 2, 9, 5)
print k
k = s.computeArea(-1,-1,1,1,-2,-2,2,2)
print k
k = s.computeArea(-2,-2,2,2,-2,-2,2,2)
print k
k = s.computeArea(-2, -2 ,2, 2 ,-3 ,-3, 3, -1)
print k
k = s.computeArea(-2, -2 ,2, 2 ,1 ,-3, 3, 3)
print k
k = s.computeArea(-2, -2 ,2, 2 ,3, 3, 4, 4)
print k