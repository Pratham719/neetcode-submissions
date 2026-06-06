class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i<=len(nums)-1:
            if val==nums[i]:
                nums.remove(nums[i])
            else:
                i+=1
        sorted(nums)
        return len(nums)
            