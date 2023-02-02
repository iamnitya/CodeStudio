class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c == '(':
                stack.append(count)
                count = 0
            else:
                count = stack.pop() + max(1, count*2)
        return count 