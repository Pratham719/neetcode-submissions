class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        res=[]
        for i in digits:
            n=n*10+i
        
        n+=1
        while n>0:
            dig=n%10
            res.append(dig)
            n//=10
            
        res.reverse()
        return res