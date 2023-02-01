class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                k = stack[-1]
                stack.append(k*2)
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(b)
                stack.append(a)
                stack.append(c)
            else:
                stack.append(int(i))
        total = 0
        for j in stack:
            total +=j
        return total
            