class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = list(map(chr, range(97, 123)))
        f = []
        for i in alphabets:
            if i in sentence:
                f.append(1)
            else:
                f.append(0)
        f_s = set(f)
        if len(f_s)>1:
            return False
        else:
            return True
