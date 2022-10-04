class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c=[]
        d=[]
        for i in range(1,a+1):
            if a%i == 0:
                c.append(i)
        for j in range(1,b+1):
            if b%j == 0:
                d.append(j)
        return (len(set(c).intersection(set(d))))