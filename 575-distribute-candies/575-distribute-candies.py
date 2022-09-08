class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        k = len(set(candyType))
        j = len(candyType)
        p = j//2
        if k<p:
            return k
        return p