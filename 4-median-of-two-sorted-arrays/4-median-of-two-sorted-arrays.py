class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        j = []
        j.extend(nums1)
        j.extend(nums2)
        j.sort()
        i = len(j)
        if len(j)%2==0:
            return ((j[i//2]+j[i//2-1])/2)
        return (j[i//2])