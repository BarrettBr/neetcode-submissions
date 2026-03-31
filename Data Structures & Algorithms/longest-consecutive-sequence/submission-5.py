class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) <= 1:
            return len(nums)
        curMax = 0
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                cur += 1
                curMax = max(cur, curMax)
            else:
                cur = 1
        return curMax