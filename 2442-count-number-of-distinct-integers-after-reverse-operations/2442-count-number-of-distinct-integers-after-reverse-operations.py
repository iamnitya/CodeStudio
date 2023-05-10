class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = []
        for i in nums:
            k = str(i)[::-1]
            nums1.append(int(k))
        nums.extend(nums1)
        return(len(set(nums)))