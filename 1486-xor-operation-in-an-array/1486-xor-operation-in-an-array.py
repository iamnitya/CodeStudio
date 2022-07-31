class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start+2*i)
        print(nums)
        x = 0
        for j in nums:
            x ^= j
        return(x)