class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) == 0:
            return 0
        prev = float('inf')
        cur_max = cur = 0
        for num in nums:
            if num-1 == prev:
                cur += 1
                cur_max = max(cur_max, cur + 1)
                prev = num
            else:
                cur = 0
                prev = num
        return max(cur_max, 1)