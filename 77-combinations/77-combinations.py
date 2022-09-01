from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        k1 = list(range(1,n+1))
        p = list(combinations(k1,k))
        return(p)