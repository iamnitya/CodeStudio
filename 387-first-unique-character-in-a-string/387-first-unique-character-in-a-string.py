class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i,m in enumerate(s):
            if m in dic:
                dic[m] = -1
            else:
                dic[m] = i
            
        for k in dic:
            if dic[k] != -1:
                return dic[k]
        return -1