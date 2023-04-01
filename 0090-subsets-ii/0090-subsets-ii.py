class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        p = []
        nums.sort()
        import itertools
        for i in range(len(nums)+1):
            k = list(itertools.combinations(nums,i))
            k1 =set(k)
            for j in k1:
                list(j).sort()
                p.append(list(j))
        p1 = list(p)
        return p1