class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag = True
        j = word.upper()
        k = word.title()
        m = word.lower()
        if word==j:
            return True
        elif word==k:
            return True
        elif word==m:
            return True
        return False