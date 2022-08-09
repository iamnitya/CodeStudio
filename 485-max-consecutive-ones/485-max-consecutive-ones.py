class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if 1 in nums:
            n = nums.index(1)
            c = 0
            j = []
            for i in range(n,len(nums)):
                if nums[i]==1:
                    c = c + 1
                    if i == len(nums)-1:
                        j.append(c)
                else:
                    j.append(c)    
                    c = 0
            print(nums.count(1))
            return max(j)
        else:
            return 0