def bubbleSort(A, printStep = False):
	l = len(A)
	for i in range(l):
		for j in range(l-i-1):
			if A[j] > A[j+1]:
				#Swap the min
				t = A[j+1]
				A[j+1] = A[j]
				A[j] =t

		if printStep:
			print 'Iter '+str(i+1),A
	return A
