import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        k = dividend/divisor
        print(k)
        if -2**31< math.trunc(k) < 2**31 - 1:
            return math.trunc(k)
        elif math.trunc(k) >= 2**31 - 1:
            return 2**31 - 1
        elif -2**31 >= math.trunc(k):
            return -2**31