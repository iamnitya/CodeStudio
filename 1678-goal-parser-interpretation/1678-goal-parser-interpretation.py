class Solution:
    def interpret(self, command: str) -> str:
        c = command.replace("()","o")
        d = c.replace("(al)","al")
        return d
        