class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        total=sum(nums)

        for i in range(len(nums)):
            cur=nums[i]
            right=total-left-cur
            if left==right:
                return i
            left+=cur
        return -1