class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            k = n
        else:
            k= (n*2)
        return k
