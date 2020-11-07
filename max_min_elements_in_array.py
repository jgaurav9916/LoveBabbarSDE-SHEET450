#User function Template for python3

class Solution:
    def middle(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
        
        return ((A+B+C)-(max(A,B,C)+min(A,B,C)))
        #code here
        #self.A = A
        #self.B=B
        #self.C=C
        #if A>B and A>C:
         #   if B <C:
          #      return C
           # else:
             #   return B
    #    elif B>A and B>C:
     #       if A > C:
     #           return A
      #      else:
       #         return C
        #else:
         #   if A > B:
          #      return A
           # else:
            #    return B
       



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends