from math import trunc
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k = num**(0.5)
        if k - trunc(k)==0:
            return True
        return False