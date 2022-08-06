class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        p = []
        l =len(arr)-1
        for i in range(len(arr)):
            if i < l:
                arr.remove(arr[0])
                k = max(arr)
                p.append(k)     
            else:
                p.append(-1)
        return p