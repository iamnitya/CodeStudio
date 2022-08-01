class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a = []
        p = []
        for i in range(left, right+1):
            p.append(i)
        print(p)
        for j in p:
            k = list(str(j))
            flag = True
            for l in k:
                if int(l)==0:
                    flag = False
                    break
                elif int(j)%int(l)==0:
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                a.append(j)
        return a