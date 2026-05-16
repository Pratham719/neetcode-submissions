class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                if sorted(s)==sorted(t):
                    output=True
                else:
                    output=False
                return output

sol=Solution()
s = "racecar"
t = "carrace"

result=sol.isAnagram(s,t)
print(result)