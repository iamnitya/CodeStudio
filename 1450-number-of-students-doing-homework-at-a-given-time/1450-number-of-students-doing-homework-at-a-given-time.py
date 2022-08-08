class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        s = 0
        for i in range(len(startTime)):
            k = range(startTime[i],endTime[i]+1)
            if queryTime in k:
                s +=1
        return s

        