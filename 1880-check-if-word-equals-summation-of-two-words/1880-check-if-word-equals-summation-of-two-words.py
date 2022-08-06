class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        k = list(map(chr, range(97, 107)))
        v = range(0,10)
        res = {k[i]: v[i] for i in range(len(k))}
        print(res)
        m = list(firstWord)
        c=""
        for n in m:
            c += str(res[n])
        # # # # print(c)
        m1 = list(secondWord)
        c1=""
        for n1 in m1:
            c1 += str(res[n1])
        # # # print(c1)
        k1 = int(c1)+int(c)
        # # print(k1)
        m2 = list(targetWord)
        c2=""
        for i2 in m2:
            c2 += str(res[i2])
        # print(c2)
        if int(c2) == k1:
            return True
        else:
            return False