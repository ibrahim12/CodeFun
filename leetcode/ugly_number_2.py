class Solution1(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n


        u = {1:True}

        i = 1
        while len(u) <= n:

            if pow(2, i) not in u:
                u[pow(2, i)] = True

            if pow(3, i) not in u:
                u[pow(3, i)] = True

            if pow(5, i) not in u:
                u[pow(5, i)] = True

            i += 1
        print u
        return u.keys()[n-1]


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n

        i2=i3=i5=0
        a2=2
        a3=3
        a5=5

        ul = [1]
        u = 1
        for i in range(1, n):
            # a2 = pow(2,i2)
            # a3 = pow(3,i3)
            # a5 = pow(5,i5)
            u = min(a2, a3, a5)

            ul.append(u)
            if u == a2:
                i2 += 1
                a2 = ul[i2]*2
                print '%sx%s' % ( ul[i2], 2)

            if u == a3:
                i3 += 1
                a3 = ul[i3]*3
                print '%sx%s' % ( ul[i3], 5)


            if u == a5:
                i5 += 1
                a5 = ul[i5]*5
                print '%sx%s' % ( ul[i5], 5)

            print (a2, a3, a5, u)

        # print ul
        return u

s = Solution()
k = s.nthUglyNumber(20)
print(k)