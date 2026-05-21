class Solution:
    def maxDifference(self, s: str) -> int:
        f = {}
        even = float('inf')
        odd = 0
        for ch in s:
            f[ch] = f.get(ch, 0) + 1

        for ch in f.values():
            if ch % 2 == 0:
                even = min(even, ch)
            else:
                odd = max(odd, ch)

        return odd - even
