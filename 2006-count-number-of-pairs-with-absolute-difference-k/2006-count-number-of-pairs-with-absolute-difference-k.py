from itertools import combinations
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        comb = list(combinations(nums,2))
        print(comb)
        c= 0
        for i in comb:
            j1 = i[0]
            j2 = i[1]
            if abs(j1-j2)==k:
                c+=1
        return c