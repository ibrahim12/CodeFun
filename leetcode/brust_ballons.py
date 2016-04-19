class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n_nums = [1] + nums + [1]
        n = len(n_nums)
        mem = [ [0]*n for _ in n_nums ]

        def calculate(start, end):

            if start + 1 == end:
                return 0

            for i in range(start+1, end-2):
                try:
                    mem[start][end] = max(mem[start][end], 1  * n_nums[i] * 1  + calculate(start, i) + calculate(i+1, end))
                except Exception, e:
                    print mem, start, end ,i

            return mem[start][end]

        return calculate(0, n)



s = Solution()
k = s.maxCoins([3, 1, 5, 8])
print k