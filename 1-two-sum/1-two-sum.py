class Solution:
    def twoSum(self, nums, target):
		
        l = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)
        return l