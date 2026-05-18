class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans=-1
        for i in range(len(nums)):
            if sum(nums[:i])==sum(nums[i+1:]):
                ans=i
                break
        return ans

sol=Solution()
arr = [1,7,3,6,5,6]
print(sol.pivotIndex(arr))
