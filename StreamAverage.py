class Solution:
	def streamAvg(self, arr, n):
		# code here
        l=[]
        s=0
        for i in range(n):
            s+=arr[i]
            l.append(s/(i+1))
        return l
