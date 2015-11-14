def knapsackProblem(weight, value, capacity):
	# As we Iterate through each item, we two choices, take it or leave it
	# So the choice should be the one which maximizes the value
	
	# Can be done in both Recursion(DP with Memoization) & Iterative DP
	
	#Iterative Solution
	maxWt = [ [0 for x in range(weight)] for x in range(weight)]
	
	
