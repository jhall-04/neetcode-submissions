class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        prev = 1
        for i in range(1, n+1):
            if 2 * prev == i:
                prev = i
            res[i] = 1 + res[i - prev]
        return res
