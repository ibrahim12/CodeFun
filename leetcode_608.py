from math import sqrt


class Solution(object):

    def find(self, n, index, c, numbers):

        if index == len(numbers):
            return c

        if n <= 0:
            return 0

        c1 = n//numbers[index]

        print n, index, c, c1
            
        return min( self.find(n%numbers[index], index+1, c + c1, numbers), 
                    self.find(n, index+1, c, numbers))

    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
                
        numbers = []
        is_prefect = {}
        is_prefect[0] = False
        for i in range(1, n+1):
            sqrti = int(sqrt(i))
            if sqrti * sqrti == i:
                is_prefect[i] = True
                numbers.append(i)
            else:
                is_prefect[i] = False
                
        numbers = numbers[::-1]

        print numbers

        return self.find(n, 0, 0, numbers)

        
        
            

a = Solution()
print(a.numSquares(6));
