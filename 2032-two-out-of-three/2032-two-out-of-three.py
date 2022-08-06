class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        num_1 = set(nums1)
        num_2 = set(nums2)
        num_3 = set(nums3)
        k = []
        n12 = num_1.intersection(num_2)
        for i in n12:
            k.append(i)
        n13 = num_1.intersection(num_3)
        for j in n13:
            k.append(j)
        n32 = num_3.intersection(num_2)
        for l in n32:
            k.append(l)
        n123 = n32.intersection(num_1)
        for p in n123:
            k.append(p)
        return (list(set(k)))
        