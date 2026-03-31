class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        diffs = {} # Num : Index
        for i, n in enumerate(nums):
            goal = target - n
            if goal in diffs:
                return [diffs[goal], i]
            
            diffs[n] = i