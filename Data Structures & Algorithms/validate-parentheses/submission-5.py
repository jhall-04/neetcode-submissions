class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}
        left= '({['
        stack = []
        for c in s:
            if stack and stack[-1] == match.get(c, -1):
                stack.pop(-1)
            else:
                stack.append(c)
        return len(stack) == 0
