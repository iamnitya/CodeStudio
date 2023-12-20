class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j=s.lower()
        k = []
        for i in j:
            if i.isalnum():
                k.append(i)
        p = k[::-1]
        if p == k:
            return True
        return False