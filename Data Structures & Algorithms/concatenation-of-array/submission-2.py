class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums+nums
        return ans


sol = Solution()
nums = [1, 4, 1, 2]
result = sol.getConcatenation(nums)
print(result)