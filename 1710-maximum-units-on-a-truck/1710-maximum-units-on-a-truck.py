class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        modified_boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse = True)
        print(modified_boxTypes)
        s = 0
        for i in modified_boxTypes:
            s1 = 1
            if i[0]<truckSize and truckSize>=0:
                s1 = i[0]*i[1]
                s+=s1
            elif truckSize>=0:
                s1 = truckSize * i[1]
                s+=s1
            truckSize -= i[0]
        return(s)