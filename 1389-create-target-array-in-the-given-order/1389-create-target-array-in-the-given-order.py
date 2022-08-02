class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        k = len(index)
        a =[]
        for i in range(k):
            b = index[i]
            c = nums[i]
            a.insert(b,c)
        return a