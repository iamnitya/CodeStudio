class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        k = []
        for i in image:
            i = i[::-1]
            k.append(i)
        p = []
        for l in k:
            m = []
            for j in l:
                if j == 1:
                    m.append(0)
                else:
                    m.append(1)     
            p.append(m)
        return p