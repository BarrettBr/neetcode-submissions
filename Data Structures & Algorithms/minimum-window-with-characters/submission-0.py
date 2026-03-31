class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def subsetCheck(dict1, dict2):
            for k,v in dict1.items():
                if dict2.get(k, 0) < v:
                    return False
            return True

        n = len(s)
        if len(s) == 0 or len(t) == 0:
            return ""
        
        tCount = {}
        for l in t:
            tCount[l] = tCount.get(l, 0) + 1
        
        ret = ""
        window = {}
        minLen, leftPointer = float("inf"), 0
        for r in range(n):
            window[s[r]] = window.get(s[r], 0) + 1
            while leftPointer <= r and subsetCheck(tCount, window):
                windowLen = (r - leftPointer) + 1
                if windowLen < minLen:
                    minLen = windowLen
                    ret = s[leftPointer:r+1]
                window[s[leftPointer]] -= 1
                leftPointer += 1
        return ret