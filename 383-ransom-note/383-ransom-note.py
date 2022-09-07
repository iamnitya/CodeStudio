class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for j in set(ransomNote):
            if magazine.count(j) < ransomNote.count(j):
                return False
        return True