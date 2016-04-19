class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^y, nums)


s = Solution()
k = s.singleNumber([2,2,1,3,1])

print k

