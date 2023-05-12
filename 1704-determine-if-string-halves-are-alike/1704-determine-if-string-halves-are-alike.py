class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s.lower()
        s1 = list(s)
        pre = s1[:len(s)//2]
        post = s1[len(s)//2::]
        pre1 = []
        post1 = []
        for i in pre:
            if i in vowels:
                pre1.append(i)
        for j in post:
            if j in vowels:
                post1.append(j)
                
        pre1.sort()
        post1.sort()
        if len(pre1)==len(post1):
            return True
        return False