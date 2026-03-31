class Solution:
    def isValid(self, s: str) -> bool:
        char = []
        for c in s:
            if c in "([{":
                char.append(c)
            elif (len(char) > 0):
                if c == ")" and (char.pop()) != "(":
                    return False
                elif c == "]" and (char.pop()) != "[":
                    return False
                elif c == "}" and (char.pop()) != "{":
                    return False
            else:
                return False
        return len(char) == 0