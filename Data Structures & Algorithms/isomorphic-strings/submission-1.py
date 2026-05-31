class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s={}
        map_t={}
        for ch_s,ch_t in zip(s,t):
            if ch_s in map_s and map_s[ch_s] != ch_t:
                return False
            if ch_t in map_t and map_t[ch_t]!=ch_s:
                return False
            map_s[ch_s]=ch_t
            map_t[ch_t]=ch_s
        return True