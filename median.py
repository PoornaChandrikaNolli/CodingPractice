class Solution:
	def find_median(self, v):
		# Code here
        v.sort()
        l=len(v)
        if l%2==1:
            return v[int((l+1)/2)-1]
        else:
            return int((v[int(l/2)]+v[int(l/2)-1])/2)
