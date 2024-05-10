class Solution:
    def reverse(self,n):
        rev=0
        while(n>0):
            rev=rev*10+n%10
            n=int(n/10)
        return rev
    def isSumPalindrome (self, n):
        # code here 
        for i in range(6):
            if n==self.reverse(n):
                return n
            n=self.reverse(n)+n
        return -1
