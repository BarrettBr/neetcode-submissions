class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l, r = 0, len(heights) - 1

        while l < r:
            val = (r - l) * min(heights[l], heights[r])
            best = max(best, val)
            if heights[l] > heights[r]:
                r -=1
                while l < r and heights[r] == heights[r+1]:
                    r -= 1
            else:
                l += 1
                while l < r and heights[l] == heights[l-1]:
                    l += 1
        return best