class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            cur = 0
            if l < r and heights[l] < heights[r]:
                cur = (r - l) * heights[l]
                l += 1
            else:
                cur = (r - l) * heights[r]
                r -= 1
            ret = max(ret, cur)
        return ret