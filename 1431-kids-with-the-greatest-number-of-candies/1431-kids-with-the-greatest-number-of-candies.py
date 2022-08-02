class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = []
        for i in candies:
            k = i+extraCandies
            # print(k)
            # print(max(candies))
            if k >= max(candies):
                a.append(True)
            else:
                a.append(False)
        print(a)
        return(a)