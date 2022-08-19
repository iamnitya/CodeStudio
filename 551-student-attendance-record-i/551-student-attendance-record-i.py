class Solution:
    def checkRecord(self, s: str) -> bool:
        l = s.count("LLL")
        a = s.count("A")
        if a>1 or l>=1:
            return False
        # elif a==0 and l>=1:
        #     return False
        # elif a>2 and l==0:
        #     return False
        return True