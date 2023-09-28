from typing import List


class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        for i in range(0,n-1,2):
                a[i],a[i+1]=a[i+1],a[i]
        return n



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        obj.convertToWave(n, a)
        IntArray().Print(a)

# } Driver Code Ends