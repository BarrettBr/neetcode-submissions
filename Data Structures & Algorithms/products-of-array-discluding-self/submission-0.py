class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        for i in range(1, n):
            output[i] = nums[i-1] * output[i-1]

        right = 1
        for num in reversed(range(n)):
            output[num] *= right
            right *= nums[num]

        return output