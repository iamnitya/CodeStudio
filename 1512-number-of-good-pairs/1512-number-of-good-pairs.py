from itertools import combinations
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        k =list(combinations(nums,2))        
        c=0
        for i in k:
            if i[0] ==i[1]:
                c+=1
        return c