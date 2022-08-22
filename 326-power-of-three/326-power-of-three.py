class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        flag = True
        while n>1:
            if n%3==0:
                flag = True
                n = n/3
            else:
                flag = False
                return False
        return True
        