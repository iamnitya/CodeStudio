class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num1 = list(str(num))
        num1.sort()
        even = ""
        odd = ""
        for i in range(len(num1)):
            if i%2==0:
                even += (num1[i])
            else:
                odd += num1[i]
        return(int(even)+int(odd))
        