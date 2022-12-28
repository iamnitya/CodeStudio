class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split(" ")
        k = ""
        print(l)
        mydict = {}
        for i in range(len(l)):
            p = l[i]
            print(p)
            num =list(p)[-1]
            val = p.replace(num,"")
            mydict[int(num)] = val
            print(val)
        for j in range (1,len(l)):
            k = k + mydict[j] + " "
        k += mydict[len(l)]
        return k