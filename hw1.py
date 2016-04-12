# python 2.7
def hw1(u, lambdavar):
	# compute u_square and lambda_square
	# set both to be float value for division
    u_square = float(u*u)
    lambda_square = float(lambdavar*lambdavar)
    
	#Case 1: when x = 0, the value of function:
    f1 = u_square
	#initialize 
	argmin_x = 0
	min_f = f1
	
    #Case 2: when x > 0, the argmin_x is:
	x2 = float(u) - float(lambdavar)/2
	f2 = u * lambdavar - lambda_square/4 #lambda_square is float value
	
	if x2 > 0: # if x1 <= 0, Case 2 can not be considered
		if f2 < min_f:
			argmin_x = x2
			min_f = f2

	#Case 3: when x < 0, the argmin_x is 
	x3 = float(u) + float(lambdavar)/2
	f3 = -1 * u * lambdavar - lambda_square/4 #lambda_square float value
	
	if x3 < 0:
		if f3 < min_f:
			argmin_x = x3
			min_f = f3
	
	return argmin_x
			
			