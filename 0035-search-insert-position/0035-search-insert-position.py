class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            k = nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            k = nums.index(target)
        return k
