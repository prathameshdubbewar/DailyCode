class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        lst = lst[::-1]
        str1 = " "
        return str1.join(lst)

    '''
    OR
    '''
    
        # return " ".join(s.split()[::-1])
        