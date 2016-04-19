class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        sorted_strs = []
        for i in range(n):
            sorted_strs.append(''.join(sorted(strs[i])))

        out = {}
        for i in range(n):
            out.setdefault(sorted_strs[i], []).append(i)

        f_out = []
        for arr in out:
            temp = []
            for index in out[arr]:
                temp.append(strs[index])
            f_out.append(sorted(temp))

        return f_out



s = Solution()
k = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# k = s.groupAnagrams(["e", "", ""])
print(k)