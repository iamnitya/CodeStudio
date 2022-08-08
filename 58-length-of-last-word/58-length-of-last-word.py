class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.split(" ")
        print(k)
        for i in range(k.count("")):
            k.remove("")
        return(len(k[-1]))