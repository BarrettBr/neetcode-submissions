class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        # Check if we can replace all
        if n <= k:
            return n
        count = {} # Letter : count
        l, res, mostFreq = 0, 0, 0
        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            windowSize = r - l + 1
            mostFreq = max(mostFreq, count[s[r]])
            while windowSize - mostFreq > k:
                count[s[l]] -= 1
                l += 1
                mostFreq = max(mostFreq, count[s[l]])
                windowSize -= 1
            res = max(res, windowSize)
        return res