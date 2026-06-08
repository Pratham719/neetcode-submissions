class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        need = hay = 0
        if needle == "":
            return 0

        while hay < len(haystack):
            if haystack[hay] == needle[need]:
                hay += 1
                need += 1
                if need == len(needle):
                    return hay - need
            else:
                hay = hay - need + 1
                need = 0
        return -1
