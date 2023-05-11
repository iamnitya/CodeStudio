class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """       
        ring = list(rings)
        p = []
        q = {}
        for i in range(0,10):
            p.append(str(i))
        for i in p:
            q[i] = ""
        for i in range(0,len(ring)-1,2):
            q[ring[i+1]] += ring[i] 
        count = 0
        for j in q.values():
            if len(set(list(j)))==3:
                count+=1
        return count