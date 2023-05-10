class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = []
        while len(nums)>1:
            p=[]
            for i in range(len(nums)-1):
                p.append((nums[i]+nums[i+1])%10)
            nums = p
        return nums[0]
