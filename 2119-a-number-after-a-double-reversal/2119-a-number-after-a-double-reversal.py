class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        k = str(num)
        p = int(k[::-1])
        q = str(p)[::-1]
        print(q)
        if int(q)==num:
            return True
        else:
            return False