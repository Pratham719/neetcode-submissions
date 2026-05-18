class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans = -1
        left = 0
        right = 0
        total = sum(nums)

        for i in range(len(nums)):
            current = nums[i]
            right = total - left - current
            if right == left:
                ans = i
                break
            left += current
        return ans


sol = Solution()
arr = [1, 7, 3, 6, 5, 6]
print(sol.pivotIndex(arr))
