class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)+1
        s=set(nums)
        res=[]

        for i in range(1,n):
            if i not in s:
                res.append(i)
        return res