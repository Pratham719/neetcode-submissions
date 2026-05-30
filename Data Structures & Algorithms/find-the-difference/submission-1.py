class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s={}
        freq_t={}

        for ch in s:
            freq_s[ch]=freq_s.get(ch,0)+1
        for ch in t:
            freq_t[ch]=freq_t.get(ch,0)+1
        
        for ch in freq_t:
            if ch not in freq_s or freq_t[ch] > freq_s.get(ch,0):
                return ch
        



        
        