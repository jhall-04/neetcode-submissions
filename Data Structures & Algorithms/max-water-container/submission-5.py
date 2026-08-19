class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        volume = 0
        while l < r:
            volume = max(volume, min(heights[l], heights[r]) * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return volume

