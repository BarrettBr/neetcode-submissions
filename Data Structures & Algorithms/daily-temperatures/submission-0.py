class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n
        stack = []
        for i, num in enumerate(temperatures):
            while len(stack) != 0 and num > temperatures[stack[-1]]:
                prev = stack.pop()
                out[prev] = i - prev
            stack.append(i)
        return out