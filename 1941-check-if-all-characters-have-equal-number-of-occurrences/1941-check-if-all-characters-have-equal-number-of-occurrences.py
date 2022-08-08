class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_s = set(list(s))
        m=[]
        for i in s_s:
            j=s.count(i)
            m.append(j)
        if len(set(m))==1:
            return True
        else:
            return False