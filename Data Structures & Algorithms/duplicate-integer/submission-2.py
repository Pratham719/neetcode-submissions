class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        return len(nums) != len(set(nums))


sol = Solution()
nums = [1, 2, 3, 4, 5, 5]
result = sol.hasDuplicate(nums)
print(result)
