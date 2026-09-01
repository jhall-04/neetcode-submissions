class Solution:
    def climbStairs(self, n: int) -> int:
        state = [0] * n
        for i in range(n):
            if i in (0, 1):
                state[i] = i+1
                continue
            state[i] = state[i-1] + state[i-2]
        return state[-1]