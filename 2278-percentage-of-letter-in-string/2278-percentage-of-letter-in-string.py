class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        s_l = list(s)
        k = s_l.count(letter)
        print((100*k/len(s_l)))
        return int((100*k/len(s_l)))