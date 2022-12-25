class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        greater_than = []
        p = []
        for i in nums:
            if i<pivot:
                less_than.append(i)
            elif i>pivot:
                greater_than.append(i)
        p.extend(less_than)
        k = nums.count(pivot)
        for ll in range(k):
            p.append(pivot)
        p.extend(greater_than)
        return p