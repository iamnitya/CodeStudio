class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        m = digits[::-1]
        print(m)
        for i in range(len(digits)):
            s += m[i]*(10**i)
        k = list(str(s+1))
        return k