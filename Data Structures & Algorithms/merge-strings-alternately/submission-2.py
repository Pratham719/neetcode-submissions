class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        l=min(len(word1),len(word2))
        m=word2 if len(word1)<len(word2) else word1

        for i in range(l):
            res+=word1[i]
            res+=word2[i]

        res+=m[l:]
        return res