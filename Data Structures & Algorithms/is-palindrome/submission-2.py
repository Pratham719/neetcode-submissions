class Solution:
    def isPalindrome(self, s: str) -> bool:

        return "".join(ch.lower() for ch in s if ch.isalnum())=="".join(ch.lower() for ch in s if ch.isalnum())[::-1]

