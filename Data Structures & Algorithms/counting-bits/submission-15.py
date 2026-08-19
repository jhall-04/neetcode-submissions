class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            cur = i
            ct = 0
            while cur > 0:
                ct += cur%2
                cur >>= 1
            res.append(ct)
        return res