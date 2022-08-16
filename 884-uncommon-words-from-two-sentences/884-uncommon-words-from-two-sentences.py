class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        k1 = s1.split(" ")
        k2 = s2.split(" ")
        j=[]
        w1 = set(k1).difference(set(k2))
        w2 = set(k2).difference(set(k1))
        for i in list(w1):
            if k1.count(i)==1:
                j.append(i)
        for i1 in list(w1):
            if k1.count(i1)==1:
                j.append(i1)
        for i2 in list(w2):
            if k2.count(i2)==1:
                j.append(i2)
        return list(set(j))