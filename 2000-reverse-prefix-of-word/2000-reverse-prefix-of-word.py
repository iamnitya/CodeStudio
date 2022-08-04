class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            ind = word.find(ch)
            w = list(word)
            k = ""
            for i in range(ind,-1,-1):
                k += w[i]
            for j in range(ind+1, len(w)):
                k += w[j]
            return k
        else:
            return word