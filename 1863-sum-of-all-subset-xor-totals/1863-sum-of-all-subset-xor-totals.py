from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        comb = []
        for i in range(len(nums)+1):
            for j in combinations (nums,i):
                comb += [list(j)]
        x = 0
        s = 0
        for i in comb:
            x = 0
            for k in i:
                x = x^k
            s = s + x
        return s