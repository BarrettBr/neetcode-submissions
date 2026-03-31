class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t or  len(s) != len(t):
            return False
        scount = {}
        tcount = {}
        for l in s:
            scount[l] = scount.get(l, 0) + 1
        
        for l in t:
            tcount[l] = tcount.get(l, 0) + 1

        return scount == tcount