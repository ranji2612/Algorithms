import random

def randPartition(A):
	#Take the first element as pivot
	l=len(A)
	#Get random element
	r = random.randrange(0,l)
	#Swap with last
	t = A[r]
	A[r] = A[l-1]
	A[l-1] = t
	#Rest is same as general quicksort
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
	print 'pivot ',p,' Start - pivot ',A[:j],' Pivot-End ',A[j+1:]
 	return A,j

def quickSort(A):
	if len(A) < 2:
		return A
	A,j = randPartition(A)
	return quickSort(A[:j]) + [A[j]] + quickSort(A[j+1:])
