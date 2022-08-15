class Solution:
    def average(self, salary: List[int]) -> float:
        a = max(salary)
        b = min(salary)
        salary.remove(a)
        salary.remove(b)
        s = 0
        for i in salary:
            s += i
        k = round(s/len(salary),5)
        return k