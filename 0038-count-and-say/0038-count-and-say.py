class Solution:
    def countAndSay(self, n: int) -> str:
        word = '1'
        for _ in range(n - 1):
            word = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', word))
        return word