class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        def reVal(num):

            if (num >= 0 and num <= 9):
                return chr(num + ord('0'))
            else:
                return chr(num - 10 + ord('A'))
        def strev(str):

            len = len(str);
            for i in range(int(len / 2)):
                temp = str[i]
                str[i] = str[len - i - 1]
                str[len - i - 1] = temp

        def fromDeci(res, base, inputNum):

            index = 0; 
            while (inputNum > 0):
                res+= reVal(inputNum % base)
                inputNum = int(inputNum / base)

            res = res[::-1]
            return res

        # Driver Coe
        inputNum = n
        base = k
        res = ""
        r = fromDeci(res, base, inputNum)
        print(r)
        s = 0
        j = list(str(r))
        for v in j:
            s = s + int(v)
        print(s)
        
        return s