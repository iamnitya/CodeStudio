class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        i = 0
        j = 0
        s = 0
        while i < len(mat) and j<len(mat):
            s += mat[i][j] + mat[i][len(mat)-1-i]
            i+=1
            j+=1
        if len(mat)%2!=0:
            return(s-mat[len(mat)//2][len(mat)//2])
        return s