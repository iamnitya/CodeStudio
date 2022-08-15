class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        k = nums[0]
        for i in nums:
            k = set(k).intersection(set(i))
        m = list(k)
        m.sort()
        return m