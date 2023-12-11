class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        k = set(arr)
        j = 0
        p = len(arr)/4
        for i in k:
            if arr.count(i)>p:
                j = i
        return j
                