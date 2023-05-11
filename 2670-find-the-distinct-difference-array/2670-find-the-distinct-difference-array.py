class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = []
        for i in range(len(nums)):
            pre = nums[:i+1]
            post = nums[i+1::]
            prefix = len(set(pre))
            suffix = len(set(post))
            k.append(prefix-suffix)
        return k