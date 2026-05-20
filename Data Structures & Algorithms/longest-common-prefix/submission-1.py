class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        perfix=""
        first=strs[0]

        for i in range(len(first)):
            ch=first[i]
        
            for word in strs:
                if i>= len(word) or word[i]!=ch:
                    return perfix
            perfix+=ch
        return perfix