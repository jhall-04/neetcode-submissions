class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in match.keys():
                stack.append(c)
            else:
                if stack and match[stack[-1]] == c:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0
