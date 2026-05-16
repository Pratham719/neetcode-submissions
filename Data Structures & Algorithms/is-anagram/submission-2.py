class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s)!=len(t):
                    return False
            else:
                f={}
                for ch in s:
                    f[ch]=f.get(ch,0)+1

                for ch in t:    
                    if ch not in f:
                        return False
                    f[ch]-=1

                return all(value==0 for value in f.values())  

sol=Solution()
s = "racecar"
t = "carrace"

result=sol.isAnagram(s,t)
print(result)