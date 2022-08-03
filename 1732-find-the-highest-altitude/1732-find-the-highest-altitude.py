class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = 0
        alt = [0]
        for i in gain:
            a +=i
            alt.append(a)
        #print(alt)
        return max(alt)
        