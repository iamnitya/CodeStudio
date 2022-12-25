class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict = {k: v for k, v in zip(heights, names)}
        print(my_dict)
        heights.sort()
        p = []
        for i in heights:
            l = my_dict[i]
            p.append(l)
        return (p[::-1])