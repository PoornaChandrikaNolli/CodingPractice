class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        if a==0:
            return b
        elif b==0:
            return a
        else:
            return self.gcd(b,a%b)
        
