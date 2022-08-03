class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split(" ")
        num = len(l)
        p=""
        if num<k:
            return s
        else:
            for i in range(k):
                if i<k-1:
                    p += l[i] + " "
                else:
                    p += l[i]
            return p