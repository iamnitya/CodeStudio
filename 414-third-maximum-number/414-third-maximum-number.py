class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))<3:
            return max(nums)
        else:
            k = list(set(nums))
            k.sort()
            return k[-3]