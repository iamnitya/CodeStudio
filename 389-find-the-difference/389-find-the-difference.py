class Solution:
       def findTheDifference(self, s: str, t: str) -> str:
        s,t = Counter(s), Counter(t)
        res = t-s
        q = res.keys()
        let = list(q)
        return let[-1]