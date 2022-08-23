class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1 = list(word1) 
        s2 = list(word2)
        l = min(len(s1),len(s2))
        k = ""
        for i in range(l):
            k += s1[i]+s2[i]
        if len(s1)>len(s2):
            for j1 in range(l,len(s1)):
                k+= s1[j1]
        elif len(s1)<len(s2):
            for j2 in range(l,len(s2)):
                k+= s2[j2]
        return k