class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        needed = [float('inf')] * (amount+1)
        needed[0] = 0
        for i in range(len(needed)):
            for c in coins:
                if i-c >= 0:
                    needed[i] = min(needed[i], needed[i-c] + 1)
        return needed[-1] if needed[-1] != float('inf') else -1
        