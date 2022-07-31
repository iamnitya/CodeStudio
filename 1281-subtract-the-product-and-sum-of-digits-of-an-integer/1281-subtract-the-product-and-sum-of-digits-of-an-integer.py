class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        for i in range(len(str(n))):
            s = s + int(str(n)[i])
            p = p * int(str(n)[i])
        return p-s