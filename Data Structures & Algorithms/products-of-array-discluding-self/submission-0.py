class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        perfix = [1] * len(nums)
        suffix = [1] * len(nums)
        answer = [1] * len(nums)

        for i in range(1, len(nums)):
            perfix[i] = perfix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            answer[i] = perfix[i] * suffix[i]

        return answer
