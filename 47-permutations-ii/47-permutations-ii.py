from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        k = list(permutations(nums,len(nums)))
        return list(set(k))