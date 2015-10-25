def quickSort(A):
	if len(A) < 2:
		return A
	#Take the first element as pivot
	l=len(A)
	p = A[l-1]
	
	j = 0
	for i in range(0,len(A)-1):
		if A[i]<p:
			#Replace i & j
			t = A[i]
			A[i] = A[j]
			A[j] = t
			#j + + 
			j+=1
	A[l-1] = A[j]
	A[j] = p
	print '---',A[:j],A[j+1:]
	return quickSort(A[:j]) + [p] + quickSort(A[j+1:])
