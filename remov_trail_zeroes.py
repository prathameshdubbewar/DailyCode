class Solution(object):
    def removeTrailingZeros(self, num):
    
        s=str(num)
        return s.rstrip("0")

                # OR

        # for i in range(len(num) - 1, -1, -1):
        #     if num[i] != '0':
        #         return num[:i+1]
        
        # return '0'
        