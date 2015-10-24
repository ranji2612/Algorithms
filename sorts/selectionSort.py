def selectionSort(A, printStep = False):
	l = len(A)
	for i in range(l-1):
		k = i
		for j in range(i+1,l):
			if A[j] < A[k]:
				k = j
		#Swap the min
		t = A[k]
		A[k] = A[i]
		A[i] =t

		if printStep:
			print 'Iter '+str(i+1),A
	return A
