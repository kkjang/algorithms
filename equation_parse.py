from __future__ import division

def solve(equation, given_x):
	coef_dict = parse_equation(equation)
	adjusted_x = (coef_dict['x'])*-1 * given_x
	coef_y = coef_dict['y']
	final = None
	if coef_dict['none']:
		final = (adjusted_x + (coef_dict['none']*-1)) / coef_y
	else:
		final = adjusted_x / coef_y
	return final


def parse_equation(equation):
	coef_dict = dict()
	eq_list = list(equation.replace(' ', ''))
	before_equal = True
	indx = 0
	while indx < len(eq_list):
		new_coef = []
		outside = False
		no_digit = True
		if eq_list[indx] is '-' or eq_list[indx] is '+':
			if eq_list[indx] is '-':
				new_coef.append('-')
			indx += 1
		while eq_list[indx].isdigit():
			no_digit = False
			new_coef.append(eq_list[indx])
			if indx == len(eq_list)-1:
				outside = True
				break
			else:
				indx += 1
		if no_digit:
			new_coef.append('1')
		if before_equal:
			new_coef = int(''.join([str(x) for x in new_coef]))
		else:
			new_coef = int(''.join([str(x) for x in new_coef])) * -1
		if eq_list[indx] is 'x' or eq_list[indx] is 'y':
			if eq_list[indx] in coef_dict:
				coef_dict[eq_list[indx]] += new_coef
			else:
				coef_dict[eq_list[indx]] = new_coef
			indx += 1
		else:
			if 'none' in coef_dict:
				coef_dict['none'] += new_coef
			else:
				coef_dict['none'] = new_coef
			if outside:
				break
			if eq_list[indx] is '=':
				before_equal = False
				indx += 1
	return coef_dict

print solve("3x-y-2=x+2y-12", 2)