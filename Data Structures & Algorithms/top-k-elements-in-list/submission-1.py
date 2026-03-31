class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or not nums:
            return []

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            buckets[value].append(key)
        
        ret = []
        for bucket in reversed(buckets):
            if k <= 0:
                return ret
            for num in bucket:
                ret.append(num)
                k -= 1
        return ret