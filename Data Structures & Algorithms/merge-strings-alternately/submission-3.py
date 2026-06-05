class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        n1,n2=len(word1),len(word2)
        min_len=min(n1,n2)

        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])

        if n1>n2:
            res.append(word1[min_len:])
        else:
            res.append(word2[min_len:])
        
        return "".join(res)