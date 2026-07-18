class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        cur_max = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum+num)
            cur_max = max(cur_max, cur_sum)
        return cur_max