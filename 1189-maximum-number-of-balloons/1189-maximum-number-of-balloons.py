class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count("b")
        a = text.count("a")
        l = text.count("l")
        o = text.count("o")
        n =  text.count("n")
        p = []
        p.append(b//1)
        p.append(a//1)
        p.append(l//2)
        p.append(o//2)
        p.append(n//1)
        return min(p)