class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p=[]
        for i in nums:
            k = i**2
            p.append(k)
        p.sort()
        return (p)
        