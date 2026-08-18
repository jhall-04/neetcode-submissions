class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        candidates = set()
        res = 0
        for u in unique:
            if u-1 not in unique:
                candidates.add(u)
        for candidate in candidates:
            cur = candidate
            i = 0
            while cur in unique:
                cur += 1
                i += 1
            res = max(i, res)
        return res
            


