class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # import math
        # seive = [True]*num
        # seive[0] = seive[1] = False
        #
        # t = int(math.sqrt(num)) + 1
        # for i in range(2, t):
        #     seive[i**i:num:i] = [False]*(len(seive[i*i::i]))
        #
        # for i in range(2, t):
        #     if seive[i]:
        #         while not (num%i):
        #             num /= i

        s = [2, 3, 5]

        for i in s:
            while (num%i) == 0 < num:
                num /= i

        return num == 1


s = Solution()
print(s.isUgly(0))
print(s.isUgly(1))
print(s.isUgly(2))
print(s.isUgly(6))
print(s.isUgly(8))
print(s.isUgly(7))