class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f'#{len(string)}#'
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = ''
                i += 1
                while s[i] != '#':
                    length += s[i]
                    i += 1
                i += 1
                length = int(length)
            strs.append(s[i:i+length])
            i += length
        return strs

