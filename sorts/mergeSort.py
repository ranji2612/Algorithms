def merge(A,B):
	i=0
	j=0
	newList = []
	while i<len(A) or j < len(B):
		if ( (j>len(B)-1) or (i<len(A) and A[i] <= B[j]) ):
			newList.append(A[i])
			i+=1
		elif ( (i>len(A)-1) or (j<len(B) and A[i] > B[j] ) ): 
			newList.append(B[j])
			j+=1
	return newList
def mergeSort(A,printStep=False):
	if printStep:
		print A
	l = len(A)
	if l < 2:
		return A
	mid = (l)/2
	#First Half
	fh = mergeSort(A[:mid],printStep)
	#Second Half
	sh = mergeSort(A[mid:],printStep)
	#merge both results
	return merge(fh,sh)
	
