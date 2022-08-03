class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabets = list(map(chr, range(97, 123)))
        k=""
        p=list(s)
        if (len(s))%2==0:
            for i in range(0,len(s),2):
                ind = alphabets.index(p[i])
                n = int(p[i+1])
                k += p[i] + alphabets[ind+n]
            return k
        else:
            for i in range(0,len(s)-1,2):
                ind = alphabets.index(p[i])
                n = int(p[i+1])
                k += p[i] + alphabets[ind+n]
            k += p[-1]
            return k
            