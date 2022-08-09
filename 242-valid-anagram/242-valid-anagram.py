class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k = list(s)
        m = list(t)
        k.sort()
        m.sort()
        if k == m:
            return True
        return False