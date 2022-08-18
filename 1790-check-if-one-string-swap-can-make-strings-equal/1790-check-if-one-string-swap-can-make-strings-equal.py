class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        k1 = list(s1)
        k2 = list(s2)
        k1.sort()
        k2.sort()
        if k1!=k2:
            return False
        b = []
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                b.append(s1[i])
        if len(b)==2:
            return True
        return False