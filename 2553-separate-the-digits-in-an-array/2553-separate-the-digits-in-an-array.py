class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        for i in nums:
            p = []
            while i>9:
                p.append(i%10)
                i = i//10
            p.append(i)
            p.reverse()
            l.extend(p)
        return(l)