class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        if n < 2:
            return n

        mc = 1
        c = 1
        for i in range(1, n):
            if abs(nums[i] - nums[i-1]) == 1:
                c += 1
            else:
                mc = max(mc, c)
                c = 1

        mc = max(mc, c)

        return mc



s = Solution()
k = s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])
print k
k = s.longestConsecutive([1,10,20,2,3,4])
print k
k = s.longestConsecutive([0,1,-1])
print k