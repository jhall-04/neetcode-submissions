class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        volume = 0
        while l < r:
            cur_vol = min(heights[l], heights[r]) * (r - l)
            volume = max(volume, cur_vol)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return volume

