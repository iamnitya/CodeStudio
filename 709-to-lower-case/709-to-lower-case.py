class Solution:
    def toLowerCase(self, s: str) -> str:
        k=""
        j=list(s)
        for i in range(len(s)):
            j[i]=j[i].lower()
            k = k + (j[i])
        return k