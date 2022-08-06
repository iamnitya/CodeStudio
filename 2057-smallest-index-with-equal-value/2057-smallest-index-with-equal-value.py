class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i%10 == nums[i]:
                return i
            elif i == len(nums)-1:
                return -1
  