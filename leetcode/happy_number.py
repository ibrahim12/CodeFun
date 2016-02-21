class Solution1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_digits(k):
            mem = []
            while k:
               mem.append(k%10)
               k /= 10

            return mem

        if n == 1:
            return True

        while n != 1:
            d = get_digits(n)
            n = sum([ _**2 for _ in d])

            if n == 4:
                return False

        return True


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n > 6:
            n = sum([int(_)**2 for _ in str(n)])

        return n == 1

s = Solution()
k = s.isHappy(19)
print(k)

