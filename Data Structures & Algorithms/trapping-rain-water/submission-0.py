class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        
        # Build Prefix
        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(height[i], prefix[i-1])

        # Build Suffix
        suffix[n-1] = height[n-1]
        for i in reversed(range(n-1)):
            suffix[i] = max(height[i], suffix[i+1])

        water = 0        
        for i in range(n):
            cur = min(suffix[i], prefix[i]) - height[i]
            water += max(0, cur)

        return water