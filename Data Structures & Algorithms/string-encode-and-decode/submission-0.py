class Solution:

    def encode(self, strs: List[str]) -> str:
        # Take a list of strs -> str and send it which is later decoded back to a list of strs
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            length = 0
            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            decoded.append(s[i:i+length])
            i += length
        return decoded