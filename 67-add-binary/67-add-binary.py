class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = int(a,2)
        b1 = int(b,2)
        s = a1+b1
        s1 = bin(s)
        k = str(s1)[2:len((str(s1)))]
        return k