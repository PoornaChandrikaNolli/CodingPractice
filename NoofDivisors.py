import math
class Solution:
    def count_divisors(self, N):
        # code here
        c=0
        if N==1:
            return 0
        if N==2:
            return 0
        for i in range(1,int(math.sqrt(N))+1):
            if N%i==0:
                if i%3==0:
                    c+=1
                if (N//i)%3==0:
                    c+=1
        if N%3==0 and  math.sqrt(N)==int(math.sqrt(N)):
            c-=1
        return c
