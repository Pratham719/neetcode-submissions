class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_duplicate_lst = list(set(nums))
        if len(nums)==len(non_duplicate_lst):
            output=False
        else:
            output=True
        return output           
        

sol=Solution()
nums=[1,2,3,4,5,5]
result=sol.hasDuplicate(nums)
print(result)