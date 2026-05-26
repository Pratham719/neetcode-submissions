class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum = 0
        j = 0
        window_sum = float("inf")

        for i in range(len(nums)):
            Sum += nums[i]

            while Sum >= target:
                window_sum = min(window_sum, i - j + 1)
                Sum -= nums[j]
                j += 1

        return window_sum if window_sum != float("inf") else 0
