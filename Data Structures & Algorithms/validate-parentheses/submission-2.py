class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {"}":"{", "]":"[", ")":"("}
        for l in s:
            if l in closing:
               if not stack or stack.pop() != closing[l]:
                    return False
            else:
                stack.append(l)
        return len(stack) == 0