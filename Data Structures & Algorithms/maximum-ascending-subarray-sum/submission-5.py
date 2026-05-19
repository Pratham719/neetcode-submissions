class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        Sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                Sum += nums[i]
            else:
                Sum = nums[i]
            max_sum=max(max_sum,Sum)
        return max_sum
