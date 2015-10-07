import os, sys
cwd = os.getcwd()
fibonacci_path = os.path.join(cwd, 'fibonacci.py')
with open(fibonacci_path, 'a') as f:
	statement = "this is a test\n"
	f.write(statement)