class Solution(object):
    def leftRigthDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = [0]
        s = 0
        for i in range(len(nums)-1):
            s+=nums[i]
            p.append(s)
        q = [0]
        r =0
        for j in range(1,len(nums)):
            r += nums[-j]
            q.append(r)
        q.reverse()
        t = []
        for k in range(len(p)):
            t.append(abs(p[k]-q[k]))
        return t