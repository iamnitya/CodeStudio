class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        c = 0
        curr_max = 0
        for _, d in properties:
            if d < curr_max:
                c += 1
            else:
                curr_max = d
        return c
