class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        j = []
        for i in range(len(coordinates)-1):
            c1 = coordinates[i]
            c2 = coordinates[i+1]
            x1 = c1[0]
            y1 = c1[1]
            x2 = c2[0]
            y2 = c2[1]
            if x2-x1!=0:
                m = (y2-y1)/(x2-x1)
                j.append(m)
            else:
                j.append("inf")
        print(j)
        k = set(j)
        if len(k)==1:
            return True
        else:
            return False