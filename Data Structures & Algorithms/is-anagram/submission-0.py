class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = 0
        ct_s = {}
        ct_t = {}
        while i < len(s):
            ct_s[s[i]] = ct_s.get(s[i], 0) + 1
            ct_t[t[i]] = ct_t.get(t[i], 0) + 1
            i += 1
        return ct_s == ct_t