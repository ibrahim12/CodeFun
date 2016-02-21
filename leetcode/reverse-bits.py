class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = []
        for i in range(32):
            bits.append( (n >> i) & 1 )

        # print bits

        result = 0
        for i in range(32):
            result += bits[31-i] * pow(2, i) 

        return result

s = Solution()
print(s.reverseBits(43261596))