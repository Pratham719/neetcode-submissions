class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        pos = len(nums) - 1

        while l<=r:
            left_square=nums[l]*nums[l]
            right_square=nums[r]*nums[r]

            if left_square>right_square:
                result[pos]=left_square
                l+=1
            else:
                result[pos]=right_square
                r-=1
            pos-=1
        return result

