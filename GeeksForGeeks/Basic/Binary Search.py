class Solution:	
	def binarysearch(self, arr, n, k):
		left, right = 0, n-1
		while left <= right:
		    mid = (left+right)//2
		    if arr[mid] == k:
		        return mid
	        elif k > arr[mid]:
	            left = mid+1
            else:
                right = mid-1
        return -1