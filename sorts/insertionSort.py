def insertionSort(A, printSteps = False):
	l = len(A)
	
	#Iterate from second element to Last
	for j in range(1,l):
		k = j
		val = A[k]
		while k>0 and A[k-1] > val:
			A[k] = A[k-1]
			k-=1
		A[k] = val
		if printSteps:
			print 'Iter '+str(j),A
	return A
