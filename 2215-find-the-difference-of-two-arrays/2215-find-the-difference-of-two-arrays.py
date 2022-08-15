class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        p=[]
        n1 = set(nums1)
        n2 = set(nums2)
        k = list(n1.difference(n2))
        p.append(k)
        l = list(n2.difference(n1))
        p.append(l)
        return p