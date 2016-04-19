class Solution1(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)

        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]

        out = []
        s = 0
        for i in range(1, n+1):

            if (i == n or nums[i] - nums[i-1] > 1):
                if i-1 != s:
                    out.append("%s->%s" % (nums[s], nums[i-1]))
                else:
                    out.append("%s" % (nums[s]))
                s = i

        return out


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        diff = [(n-i, n) for i, n in enumerate(nums)]
        first, last = dict(diff[::-1]), dict(diff)
        print(diff)
        print(diff[::-1])
        print(first)
        print(last)
        print(`n` + ('->'+`last[d]`)*(n<last[d]))
        # return [`n` + ('->'+`last[d]`)*(n<last[d]) for d, n in sorted(first.items())]




s = Solution()
k = s.summaryRanges([1, 2, 3, 5,7])
print k