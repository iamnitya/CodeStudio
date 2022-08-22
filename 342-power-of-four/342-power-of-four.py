class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        flag = True
        while n>1:
            if n%4==0:
                flag = True
                n = n/4
            else:
                flag = False
                return False
        return True
        