class Solution(object):
    def isAnagram(self, s, t):
        k = list(s)
        m = list(t)
        k.sort()
        m.sort()
        if k == m:
            return True
        return False