class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        k = []
        for i in nums:
            if i %2==0:
                even.append(i)
            else:
                odd.append(i)
        for j in range(len(nums)//2):
            k.append(even[j])
            k.append(odd[j])
        return k