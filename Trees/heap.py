class Heap(object):
	def __init__(self, A,type = 'max'):
		self.val = A
		self.type = type
		if type == 'max':
			self.buildMaxHeap()
		else:
			self.buildMinHeap()

	
	def __parent(self,i):
		return i/2

	def __left(self,i):
		return 2*i + 1
	
	def __right(self,i):
		return 2*i + 2
	
	def maxHeapify(self,i):
		A = self.val
		l = self.__left(i)
		r = self.__right(i)
		largest = i
		if l < len(A) and A[l] > A[i]:
			largest = l
		if r < len(A) and A[r] > A[largest]:
			largest = r
		if largest != i:
			#Swap the nodes and call maxHeapify again
			t = self.val[largest]
			self.val[largest] = self.val[i]
			self.val[i] = t
			self.maxHeapify(largest)
	
	def minHeapify(self,i):
		A = self.val
		l = self.__left(i)
		r = self.__right(i)
		smallest = i
		if l < len(A) and A[l] < A[i]:
			smallest = l
		if r < len(A) and A[r] < A[smallest]:
			smallest = r
		if smallest != i:
			#Swap the nodes and call minHeapify again for the child subtree
			t = self.val[smallest]
			self.val[smallest] = self.val[i]
			self.val[i] = t
			self.minHeapify(smallest)
	
	def buildMaxHeap(self):
		l = len(self.val)
		for i in range(l/2,-1,-1):
			self.maxHeapify(i)
	
	def buildMinHeap(self):
		l = len(self.val)
		for i in range(l/2,-1,-1):
			self.minHeapify(i)
	
	def insert(self,x):
		return

	def delete(self,x):
		return

	def printHeap(self):
		print self.val

	def printTree(self):
		import math
		h = int(math.ceil(math.log(len(self.val)+1,2)))
		sp = int(math.pow(h,2))

		for i in range(h):
			sp -=1
			print ''.join([' ' for x in range(sp)]),((self.val[int(math.pow(2,i))-1: int(math.pow(2,i+1))-1]))
			
