class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            need = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < need:
                    l += 1
                elif nums[l] + nums[r] > need:
                    r -= 1
                else:
                    res.add(tuple(sorted((nums[i], nums[l], nums[r]))))
                    r -= 1
                    l += 1
        return [list(r) for r in res]
                    

            

        