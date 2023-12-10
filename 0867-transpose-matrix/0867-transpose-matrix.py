class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
                """
        i = len(matrix)
        j = len(matrix[0])
        k=[]
        l=[]
        for a in range(j):
            k = []
            for b in range(i):
                k.append((matrix[b][a]))
            l.append(k)
        return l