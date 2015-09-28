def fibonacci(val):
	if val == 0:
		return 0
	if val == 1:
		return 1
	return fibonacci(val-1) + fibonacci(val-2)