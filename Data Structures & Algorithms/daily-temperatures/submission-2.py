class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for cur in range(len(temperatures)):
            while stack and temperatures[cur] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = cur - prev
            stack.append(cur)
        return res
