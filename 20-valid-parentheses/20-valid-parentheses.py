class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(" : ")" ,"[" :"]","{" :"}"}
        stack = []
        if len(s) % 2 !=0:
            return False
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if(len(stack) and dic[stack[-1]]==i):
                    del stack[-1]
                else:
                    return False
        return stack == []