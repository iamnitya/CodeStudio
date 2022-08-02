class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(0,len(nums),2):
            val = (nums[i+1])
            freq = (nums[i])
            for j in range(freq):
                a.append(val)
        return(a)