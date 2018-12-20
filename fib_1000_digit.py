#https://projecteuler.net/problem=25
# needs to be iterative or else max recursion
from math import log

def fib_num_digits(num_digits):
	memo = {0:0, 1:1}
	i = 2
	while True:
		val = memo[i-1] + memo[i-2]
		if get_digits(val) == 1000:
			break
		memo[i] = val
		i += 1
	print(i)
	return val 
	

def get_digits(n):
	if n == 0:
		return 1
	return int(log(n, 10)) + 1 

fib_num_digits(1000)
