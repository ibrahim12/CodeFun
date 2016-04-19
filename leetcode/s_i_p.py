class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)

        l = 0
        h = n-1
        while l <= h:
            m = (l+h) >> 1

            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                h = m-1
            else:
                return m

        return l

s = Solution()
k = s.searchInsert([1, 3, 4, 7], 10)
print k