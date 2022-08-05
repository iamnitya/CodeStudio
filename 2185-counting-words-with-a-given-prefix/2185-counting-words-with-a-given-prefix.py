class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        k = len(pref)
        for i in words:
            if i[0:k]==pref:
                count +=1
        return count