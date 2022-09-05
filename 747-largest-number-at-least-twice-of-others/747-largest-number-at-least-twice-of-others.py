class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        k = max(nums)
        p = nums.index(k)
        nums.remove(k)
        for i in nums:
            if i*2>k:
                return -1
        return p