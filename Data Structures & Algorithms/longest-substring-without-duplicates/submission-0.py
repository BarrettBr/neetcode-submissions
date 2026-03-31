class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == n:
            return n
        bestSubstring = 0
        l = 0
        seen = {s[l]}
        for r in range(1, n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            bestSubstring = max(len(seen), bestSubstring)
        return bestSubstring