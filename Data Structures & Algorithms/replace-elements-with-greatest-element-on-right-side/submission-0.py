class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr=[]
        for i in range(len(arr)-1):
            right_side=arr[i+1:]
            new_arr.append(max(right_side))
        new_arr.append(-1)
        return new_arr    
          
sol=Solution()
arr = [2,4,5,3,1,2]
print(sol.replaceElements(arr))