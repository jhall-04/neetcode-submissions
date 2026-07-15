class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i, n in enumerate(nums):
            if n in needs:
                return [needs[n], i]
            else:
                needs[target-n] = i
        