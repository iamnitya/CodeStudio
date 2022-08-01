class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = []
        if n == 1:
            a.append(0)
        elif n%2!=0:
            for i in range(-n//2+1,n//2+1):
                a.append(i)
        elif n%2 == 0:
            for i in range(-n//2,n//2+1):
                a.append(i)
            a.remove(0)
        return a