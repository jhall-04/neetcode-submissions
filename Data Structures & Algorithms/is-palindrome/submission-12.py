class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join([char.lower() for char in s if char.isalnum()])
        l = 0
        r = len(clean) - 1
        while l <= r:
            if clean[l] == clean[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        return True
        