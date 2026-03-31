class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = -1
        i = 0
        while (i < len(numbers)):
            curSum = numbers[i] + numbers[l]
            if target - curSum == 0:
                return [i+1, len(numbers)+l+1]
            elif target - curSum > 0:
                i += 1
            else:
                l -= 1