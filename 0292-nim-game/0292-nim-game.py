class Solution:
    def canWinNim(self, n: int) -> bool:
        k = True
        if n%4==0:
            k = False
        return k