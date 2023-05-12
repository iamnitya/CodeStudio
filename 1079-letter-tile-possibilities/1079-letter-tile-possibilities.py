class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        j = list(tiles)
        k=[]
        from itertools import permutations
        for i in range(1,len(tiles)+1):
            l=(permutations(j,i))
            k.extend(l)
        return len(set(k))