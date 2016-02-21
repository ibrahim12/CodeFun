class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        import sys
        n = len(nums)
        s_c = 0
        mem = []

        for i in range(n - 1):
            if nums[i] == 0:
               s_c += 1
               mem.append([i+1, s_c])

        # print mem

        if len(mem) != n:

            k = len(mem)
            for j in range(k):
                item = mem[j]
                p = item[0]
                if nums[p] != 0:
                    s_c = item[1]
                    while ( j != k-1 and p < mem[j+1][0]) or ( j == k -1 and p < n):
                        nums[p-s_c] = nums[p]
                        p += 1

            p = n-k
            while p < n:
                nums[p] = 0
                p += 1


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        import sys
        n = len(nums)
        c = 0
        for i in range(n):
            if nums[i] != 0:
                temp = nums[c]
                nums[c] = nums[i]
                nums[i] = temp
                c += 1




nums = [1, 0]
# nums = [0, 1, 0, 3, 12]
# print(nums)
s = Solution()
s.moveZeroes(nums)

print(nums)