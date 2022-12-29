class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k = set(list(allowed))
        count = 0
        for i in words:
            p = set(list(i))
            flag = False
            for j in p:
                if j in k:
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                count+=1
        return count