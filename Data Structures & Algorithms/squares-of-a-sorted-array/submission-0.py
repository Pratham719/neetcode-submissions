class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new=[]
        for n in nums:
            new_n=n*n
            new.append(new_n)

        return sorted(new)

