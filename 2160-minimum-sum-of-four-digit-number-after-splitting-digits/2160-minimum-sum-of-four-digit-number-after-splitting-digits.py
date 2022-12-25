class Solution:
    def minimumSum(self, num: int) -> int:
        k = list(str(num))
        k.sort()
        a = int(k[0])*10+int(k[3])
        b = int(k[1])*10+int(k[2])
        return (a+b)
