class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            while stack and temp >= stack[-1][1]:
                stack.pop()

            if stack:
                res[i] = stack[-1][0] - i
            stack.append((i, temp))
        return res