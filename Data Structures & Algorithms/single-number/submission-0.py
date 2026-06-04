class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f={}

        for n in nums:
            f[n]=f.get(n,0)+1

        for i in f:
            if f[i]==1:
                return i