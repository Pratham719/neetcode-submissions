class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    index.append(i)
                    index.append(j)
        return index



sol=Solution()
nums=[8,7,6,4]
target=13
result=sol.twoSum(nums,target=13)