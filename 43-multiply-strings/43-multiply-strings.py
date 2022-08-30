class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        k1 = 0
        p1 = list(num1)
        for i1 in range(len(p1)):
            k1 += int(p1[i1])*(10**(len(p1)-i1-1))
        k2 = 0
        p2 = list(num2)
        for i2 in range(len(p2)):
            k2 += int(p2[i2])*(10**(len(p2)-i2-1))
        k = k1*k2
        return str(k)
            