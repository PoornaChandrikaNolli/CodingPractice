class Solution:
    def armstrongNumber (self, n):
        # code here 
        s=0
        num=n
        while(n>0):
            x=n%10
            s+=x**3
            n=int(n/10)
        if s==num:
            return "Yes"
        else:
            return "No"
