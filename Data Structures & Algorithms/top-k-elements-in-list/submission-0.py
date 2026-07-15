class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for _ in range(len(nums))]
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for key, value in counts.items():
            buckets[value-1].append(key)
        top_k = []
        for b in buckets[::-1]:
            for n in b:
                k -= 1
                top_k.append(n)
                if k == 0:
                    return top_k