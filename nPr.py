class Solution:
    def factorial(self,n):
        l=[1]
        s=1
        for i in range(1,n+1):
            s=s*i
            l.append(s)
        return l
    def nPr(self, n, r):
        # code here
        x=self.factorial(n)
        return x[n]//x[n-r]
        
