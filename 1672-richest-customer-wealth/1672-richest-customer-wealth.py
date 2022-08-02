class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        tot = []
        for i in accounts:
            s = 0
            for j in i:
                s = s + j
            tot.append(s)
        return max(tot)
        