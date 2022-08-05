class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        k = set(nums)
        print(k)
        for i in k:
            j = nums.count(i)
            if j%2!=0:
                 return False
        return True