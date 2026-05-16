class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        index=[]
        for i in range(len(nums)):
            needed=target-nums[i]
            if needed in seen:
                index.append(seen[needed])
                index.append(i)  
            else:
                seen[nums[i]]=i
        return index

sol=Solution()
nums=[8,7,6,4]
target=13
result=sol.twoSum(nums,target=13)