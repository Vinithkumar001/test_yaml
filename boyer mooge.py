# Python implementation for the above approach

# Function to find majority element
def findMajority(arr, n):
	candidate = -1
	votes = 0
	
	# Finding majority candidate
	for i in range (n):
		if (votes == 0):
			candidate = arr[i]
			votes = 1
		else:
			if (arr[i] == candidate):
				votes += 1
			else:
				votes -= 1
	count = 0
	
	# Checking if majority candidate occurs more than n/2
	# times
	for i in range (n):
		if (arr[i] == candidate):
			count += 1
			
	if (count > n // 2):
		return candidate
	else:
		return -1

# Driver Code

arr = [ 22,22,11,11,22,11,11]
n = len(arr)
majority = findMajority(arr, n)
print(" The majority element is :" ,majority)
	
# This code is contributed by shivanisinghss2110
