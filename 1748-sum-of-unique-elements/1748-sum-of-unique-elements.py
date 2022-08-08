class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_s = list(set(nums))
        s = 0
        for i in nums_s:
            if nums.count(i)==1:
                s+=i
        return s