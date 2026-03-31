class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        s1Count = {}
        for l in s1:
            s1Count[l] = s1Count.get(l, 0) + 1
        

        for l in range(len(s2)-n+1):
            subString = s2[l:l+n]
            
            ssCount = {}
            for l in subString:
                ssCount[l] = ssCount.get(l, 0) + 1
            
            if ssCount == s1Count:
                return True

        return False