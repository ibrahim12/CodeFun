class Solution:

    def getLCS(self, a, b):
        na = len(a)
        nb = len(b)

        L = [ [0 for x in range(nb+1)] for y in range(na+1)]

        traces = []
        for i in range(1, na+1):
            for j in range(1, nb+1):
                if a[i-1] == b[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max( L[i][j-1], L[i-1][j] )



        all_lcs = []
        def findAllLCS(a, b, i, j):

            na = len(a)
            nb = len(b)

            if i == na or j == nb:
                return ''

            if a[i] == b[j]:
                a_lcs = findAllLCS(a, b, i+1, j+1)
                if a_lcs:
                    all_lcs.append(a_lcs)
                return all_lcs
            else:
                a_lcs = findAllLCS(a, b, i, j+1)
                b_lcs = findAllLCS(a, b, i+1, j)




        # i=na
        # j=nb
        # while i > 0 and j > 0:
        #
        #     if a[i-1] == b[j-1]:
        #         traces.append(a[i-1])
        #         i -= 1
        #         j -= 1
        #     else:
        #         if L[i-1][j] > L[i][j-1]:
        #             i -= 1
        #         else:
        #             j -= 1
        #
        # for i in range(na+1):
        #     print L[i]
        # print traces

        return L[na][nb]


s = Solution()
k = s.getLCS("abdabcd", "cdada")

print k