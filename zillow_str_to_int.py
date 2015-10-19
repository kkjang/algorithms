'''
Name: Kevin Jang
Notes: Designed as close as possible to the problem description, thus
    check_information_loss only checks for letters or decimal points.
'''
import re
def parse_long(str):
    try:
        check_valid_input(str)
        return convert_str_to_int(str)
    except ValueError as e:
        raise
        
# Check for any letters or decimal points in input string
def check_valid_input(str):
    if re.search("[a-zA-z\. ]", str):
        raise ValueError('Incorrect input string.')
        
# Check if there are two or more plus/minus signs
# or if plus/minus signs come after any digit.
def check_information_loss(str):
    if re.search("[-+]{2,}", str) or re.search("[0-9][-+]", str):
        raise ValueError('Information loss. Check plus/minus signs.')

# Converts the str into an integer by iterating through the string
def convert_str_to_int(str):
    check_information_loss(str)
    value = 0
    multiplier = 1
    sign = 1
    if str[0] is '-':
        sign = -1
    for char in str[::-1]:
        char_value = ascii_conversion(char)
        if char_value is not None:
            value += char_value * multiplier
            multiplier *= 10
    return value * sign
        
# Looks up ascii decimal values of characters.
# Only returns values for characters representing integers.
# Plus/minus signs return None, other signs throw exceptions
def ascii_conversion(char):
    if ord(char) >= 48 and ord(char) <= 57:    
        return ord(char) - 48
    elif ord(char) == 43 or ord(char) == 45:
        return None
    else:
        raise ValueError('Information loss. Improper Signs.')
        