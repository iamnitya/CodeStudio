class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        k1 = list(num1)
        m1 = k1[::-1]
        s1 = 0
        for i1 in range(len(k1)):
            s1 += int(m1[i1])*(10**i1)
        k2 = list(num2)
        m2 = k2[::-1]
        s2 = 0
        for i2 in range(len(k2)):
            s2 += int(m2[i2])*(10**i2)
        return str(s1+s2)