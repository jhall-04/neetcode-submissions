class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.dfs(nums, 0, memo)
        
    def dfs(self, nums, i, memo):
        if i > len(nums)-1:
            return 0
        if i in memo:
            return memo[i]
        skip = self.dfs(nums, i+1,memo)
        stay = nums[i] + self.dfs(nums, i+2, memo)
        memo[i] = max(skip, stay)
        return memo[i]