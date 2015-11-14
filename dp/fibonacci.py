def getFiboForN(n):
	a = 0
	b = 1
	if n==1:
		c = a
	elif n == 2:
		c = b
	for i in range(2,n):
		c = a + b
		a = b
		b = c
	return c
