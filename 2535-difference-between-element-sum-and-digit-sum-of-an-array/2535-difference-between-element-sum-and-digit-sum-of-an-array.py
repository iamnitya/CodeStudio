class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elementsum = 0
        digitsum = 0
        for i in nums:
            elementsum += i

        for i in nums:
            if i<=9:
                digitsum+=i
            else:
                while i>9:
                    digitsum += i%10
                    i = i//10
                digitsum+=i
        return abs(digitsum-elementsum)