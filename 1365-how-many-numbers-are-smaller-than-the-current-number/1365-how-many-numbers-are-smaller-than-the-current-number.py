class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            p = nums
            l = 0
            for j in p:
                if j<i:
                    l = l+1
            a.append(l)
        return a