class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        k = []
        for j in range(len(pos)):
            k.append(pos[j])
            k.append(neg[j])
        return k