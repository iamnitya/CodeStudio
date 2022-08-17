class Solution:
    def hammingWeight(self, n: int) -> int:
        m = bin(n).count("1")
        return m