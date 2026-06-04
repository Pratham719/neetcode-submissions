class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)+1
        res=[]

        for i in range(1,n):
            if i not in nums:
                res.append(i)
        return res