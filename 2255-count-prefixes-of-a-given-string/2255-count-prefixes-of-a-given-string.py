class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c = 0
        p=[]
        for i in range(1,len(s)+1):
            k = s[0:i]
            p.append(k)
        for i in words:
            if i in p:
                c +=1
        return c