class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        p = []
        for i in sentences:
            k = len(list(i.split(" ")))
            p.append(k)
        return max(p)
        