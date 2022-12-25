class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        k = []
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort()
        odd = odd[::-1]
        
        for j in range(len(nums)//2):
            k.append(even[j])
            k.append(odd[j])
        if len(nums)%2!=0:
            k.append(even[-1])
        return k