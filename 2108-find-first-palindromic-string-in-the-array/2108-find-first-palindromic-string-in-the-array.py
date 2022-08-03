class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if list(i)==list(i)[::-1]:
                return i
        return ""