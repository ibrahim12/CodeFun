
import time


class TimeIt:
    start_time = 0
    end_time = 0
    @staticmethod
    def start():
        TimeIt.start_time =  time.clock()

    @staticmethod
    def stop():
        TimeIt.end_time = time.clock()

    @staticmethod
    def duration():
        return TimeIt.end_time - TimeIt.start_time

class Solution1(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0

        seive = [True] * (n)
        seive[0] = seive[1] = False

        rt = int(math.sqrt(n))+1
        for p in range(2, rt):
            if seive[p]:
                seive[p*p:n:p] = [False]* ( len(seive[p*p::p]) )

        return sum(seive)

import math

class Solution(object):

    def is_prime(self, k):
        for i in range(2, k):
            if (k%i) == 0:
                return False
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2:
            return 0

        c = 0
        for i in range(2, n):
            if ( self.is_prime(i)):
                c += 1

        return c



# s = Solution()
#
# TimeIt.start()
# c = s.countPrimes(499979)
# TimeIt.stop()
# print(c, TimeIt.duration())
#

s = Solution1()
TimeIt.start()
c = s.countPrimes(1500000)
TimeIt.stop()
print(c, TimeIt.duration())
