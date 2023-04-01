class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        p = []
        nums.sort()
        import itertools
        for i in range(len(nums)+1):
            k = list(itertools.combinations(nums,i))
            for j in k:
                p.append(list(j))
        p1 = list(p)
        return p1