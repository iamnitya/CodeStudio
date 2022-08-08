from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        k = []
        for i in range(0,len(arr)+1):
            for j in range(i,len(arr)+1):
                m = arr[i:j]
                if len(m)%2!=0:
                    k.append(m)
        print(k)
        for j in k:
            for l in j:
                s += l
        return s
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
comb = []
        k = 0
        for i in range(len(arr)+1):
            for j in combinations(arr, i):
                comb += [list(j)]
                if len(list(j))%2!=0:
                    print(list(j))
                #     for a in range(len(list(j))):
                #         k = k + list(j)[a]
        return k
'''
        