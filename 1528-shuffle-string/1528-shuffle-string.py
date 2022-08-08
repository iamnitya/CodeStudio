class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_l = list(s)
        q = {}
        p=""
        for i in range(len(indices)):
            q[indices[i]]=s_l[i]
        print(q)
        for j in range(len(indices)):
            p += q[j]
        return p