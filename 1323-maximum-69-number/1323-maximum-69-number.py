class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        k = list(s)
        print(k)
        nums=[num]
        p =""
        for i in range(len(k)):
            if k[i]=="9":
                k[i] = "6"
            else:
                k[i] = "9"
            p =""
            for j in range(len(k)):
                p = p + k[j] 
            nums.append(int(p))
            k = list(s)
        print(nums)
        return max(nums)