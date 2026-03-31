class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        groups = {}
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count) # Key version of count

            if key not in groups:
                groups[key] = []
            
            groups[key].append(s)
        
        return list(groups.values())