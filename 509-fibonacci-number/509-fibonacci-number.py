class Solution:
    def fib(self, n: int) -> int:
        k=[0, 1]
        if n<2:
            return k[n]
        n1, n2 = 0, 1
        if n>=2:
            for i in range(2, n+1):
                n3 = n1 + n2
                k.append(n3)
                n1 = n2
                n2 = n3
            print(k)
            return(k[n-1]+k[n-2])