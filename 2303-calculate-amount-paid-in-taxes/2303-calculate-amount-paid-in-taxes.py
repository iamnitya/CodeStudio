class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        prev=sol=0
        for x,y in brackets:
            t, prev = min(x,income)-prev, x
            if t<0:break
            sol+=t*y/100
        return sol

