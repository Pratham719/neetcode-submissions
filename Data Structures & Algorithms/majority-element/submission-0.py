class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = {}
        for i in nums:
            f[i] = f.get(i, 0) + 1

        majority = sorted(f.items(), key=lambda x: x[1], reverse=True)

        return majority[0][0]
