class Solution:
    def reverseWords(self, s: str) -> str:
        p = s.split(" ")
        q = []
        r = ""
        for i in p:
            q.append(i[::-1])
        for j in q[0:len(q)-1]:
            r += j + " "
        r += q[len(q)-1]
        return r