class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        flag = True
        while n>1:
            if n%2==0:
                flag = True
                n = n/2
            else:
                flag = False
                return False
        return True
        