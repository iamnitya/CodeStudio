class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        p = []
        for i in set(arr):
            p.append(arr.count(i))
        print(p)
        if len(p)<=len(set(p)):
            return True
        return False
