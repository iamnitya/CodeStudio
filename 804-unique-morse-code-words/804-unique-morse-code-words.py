class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        test_keys = list(map(chr, range(97, 123)))
        test_values = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
        k=[]
        for i in words:
            l=""
            m = list(i)
            for j in m:
                l +=res[j]
            k.append(l)
        return (len(set(k)))