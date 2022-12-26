class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        x = 0
        for i in arr1:
            x = x^i
        y = 0
        for j in arr2:
            y = y^j
        p = x&y
        return p