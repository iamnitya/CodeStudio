class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max(nums)
        min1 = min(nums)
        nums.remove(max1)
        nums.remove(min1)
        max2 = max(nums)
        min2 = min(nums)
        val = (max1*max2)-(min1*min2)
        return val