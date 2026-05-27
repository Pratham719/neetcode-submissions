class Solution:
    def isValid(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        pairs = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif ch in pairs.values():
                if not stack:
                    return False
                if ch == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack
