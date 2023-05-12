class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        start,end = s.split(":")
        startletter = start[0]
        startnumber = start[1]
        endletter = end[0]
        endnumber = end[1]
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        startindex = alphabets.index(startletter)
        endindex = alphabets.index(endletter)
        letters = []
        for j in range(startindex,endindex+1):
            letters.append(alphabets[j])
        p = []
        for currentletter in letters:
            for i in range(int(startnumber),int(endnumber)+1):
                p.append(currentletter+str(i))
        return p