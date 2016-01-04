# Assuming input is a list and elements of list are strings and other arrays(of strings and/or arrays)
def flatten(arr):
	if not isinstance(arr, list):
		raise ValueError("Please input a list.")
	final_arr = []
	for i in arr:
		if isinstance(i, list):
			final_arr += flatten(i)
		else:
			if isinstance(i, str):
				final_arr.append(i)
			else:
				raise ValueError("List or sublist element is not a string.")
	return final_arr
