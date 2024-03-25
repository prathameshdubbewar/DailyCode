class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        ugly = [2,3,5]

        if n<=0:
            return False

        for p in ugly:
            while n % p == 0:
                n /= p
        return n == 1
        
    # OR


        # if n <= 0:
        #     return False
        
        # while n % 2 == 0:
        #     n //= 2
            
        # while n % 3 == 0:
        #     n //= 3
            
        # while n % 5 == 0:
        #     n //= 5
                
        # return n == 1
            