class Solution:
    def arrangeCoins(self, n: int) -> int:
        high, low = n, 1

        while low <= high:
            mid = (low + high) // 2
            coin = mid * (mid + 1) // 2

            if coin == n:
                return mid
            elif coin < n:
                low = mid + 1
            else:
                high = mid - 1
        return high
