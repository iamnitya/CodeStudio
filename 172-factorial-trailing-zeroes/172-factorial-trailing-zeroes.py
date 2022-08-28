import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        k = math.factorial(n)
        c = 0
        while k>1:
            if k%10==0:
                c+=1
                k = k//10
            else:
                break
        return c