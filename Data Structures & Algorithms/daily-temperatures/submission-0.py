class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        next_largest_index=0
        cur=0
        for cur in range(len(temperatures)):
            ans=0
            for future in range(cur+1,len(temperatures)):
                if temperatures[cur] < temperatures[future]:
                    ans=future-cur
                    break
            res.append(ans)
                
        return res