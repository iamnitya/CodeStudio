class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        if s[0] == "#":
            s = s[1:]
        if t[0] == "#":
            t = t[1:]
        for i in s:
            if i=="#":
                if len(stack)!=0:
                    stack.pop()            
            else:
                stack.append(i)
        s1 = ""
        for j in stack:
            s1 +=j
        stack = []
        for k in t:
            if k=="#":
                if len(stack)!=0:
                    stack.pop()
            else:
                stack.append(k)
        t1 = ""
        for l in stack:
            t1 +=l
        print(s1)
        print(t1)
        if t1 == s1:
                return True
        return False